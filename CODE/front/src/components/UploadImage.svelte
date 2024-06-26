<script lang="ts">
	import { onMount } from 'svelte';
	import axios from 'axios';
	import Loader from './Loader.svelte';
	import { API, getCookie } from '../Utils/function';
	import { createEventDispatcher } from 'svelte';
	import type { HistoriaData } from '../Models/HistoriaData';

	let predicted_classes: string;
	let promise: Promise<any>;
	let confidence: number;
	let historia: HistoriaData;

	const dispatch = createEventDispatcher();

	function enviarMensajeAlPadre() {
		dispatch('addHistory', historia);
		dispatch('viewConfidence', confidence);
	}

	function encontrarCategoriaMaxima(categorias: any) {
		let maxConfidence = -1;
		let categoriaMaxima = null;

		for (const categoria in categorias) {
			if (categorias.hasOwnProperty(categoria)) {
				const confidence = categorias[categoria].confidence;

				if (confidence > maxConfidence) {
					maxConfidence = confidence;
					categoriaMaxima = categoria;
				}
			}
		}

		return maxConfidence;
	}

	async function classifyImage(result: string) {
		const imageBase64 = result.split(',')[1];

		// Configurar los parámetros para la llamada a la API con Axios
		const url = 'https://classify.roboflow.com/plagues-cwxwv/1';
		const apiKey = 'f1lBp5ksVVfqqMhci32v';
		const headers = {
			'Content-Type': 'application/x-www-form-urlencoded'
		};

		const params = {
			api_key: apiKey
		};

		try {
			// Realizar la llamada a la API con Axios
			const response = await axios.post(url, imageBase64, {
				params: params,
				headers: headers
			});

			// Verificar si la respuesta es exitosa
			predicted_classes = response.data;
			confidence = encontrarCategoriaMaxima(response.data.predictions);
			return [predicted_classes, confidence];
		} catch (error: any) {
			// Manejar errores
			console.error('Error en la llamada a la API:', error.message);
			return [];
		}
	}

	async function postHistoria(data: HistoriaData, selectedFile: File): Promise<void> {
		const url = 'http://localhost:8000/historias/';

		// Obtener el token de acceso de la cookie
		const access_token = getCookie('access_token');

		// Agregar el token al encabezado de la solicitud
		const headers = new Headers({
			Authorization: `Bearer ${access_token}`, // Agregar el token al encabezado
			'Content-Type': 'application/json' // Establecer el tipo de contenido según tus necesidades
		});

		const requestOptions: RequestInit = {
			method: 'POST',
			headers: headers,
			body: JSON.stringify(data)
		};

		try {
			const response = await fetch(url, requestOptions);

			if (!response.ok) {
				// Si la respuesta no es exitosa, lanzar un error
				const errorText = await response.text();
				throw new Error(`Error en la solicitud: ${errorText}`);
			} else {
				const data = await response.json();
				historia = data;
				// console.log('Historia', historia);
				const formData = new FormData();
				formData.append('file', selectedFile);

				const resp = await fetch('http://localhost:8000/api/historia/image/' + historia.id, {
					method: 'POST',
					body: formData,
					headers: {
						Authorization: `Bearer ${access_token}` // Agregar el token al encabezado
					}
				});

				if (!resp.ok) {
					const errorText = await resp.text();
					throw new Error(`Error en la solicitud: ${errorText}`);
				}

				enviarMensajeAlPadre();
			}

			// console.log('Solicitud exitosa');
			// location.reload();
		} catch (error: any) {
			console.error(error.message);
			throw error; // Puedes manejar el error o relanzarlo según tus necesidades
		}
	}

	async function handleFileSelect(event: Event) {
		const input = event.target as HTMLInputElement;

		if (input.files && input.files.length > 0) {
			let selectedFile: File | null = input.files[0];
			const allowedTypes = ['image/jpeg', 'image/jpg'];
			if (!allowedTypes.includes(selectedFile.type)) {
				alert('Por favor selecciona un archivo JPG o JPEG.');
				selectedFile = null;
			}

			// Leer el contenido del archivo como base64
			const reader = new FileReader();
			reader.onloadend = async function () {
				const result = reader.result as string | null;
				let blanco_biologico: string;
				let intensidad: string;
				if (result) {
					promise = classifyImage(result);
					promise.then(async (res) => {
						const data = res[0].predicted_classes;
						if (data.length <= 1) {
							blanco_biologico = 'healthy';
							intensidad = '';
						} else {
							({ blanco_biologico, intensidad } = clasificarResultados(data));
						}

						// console.log(blanco_biologico, intensidad);
						const historiaData: HistoriaData = {
							fecha: new Date().toISOString(),
							intensidad: intensidad,
							blanco_biologico: blanco_biologico,
							id: ''
						};

						await postHistoria(historiaData, selectedFile);
					});
				}
			};

			// Leer el contenido del archivo como base64
			reader.readAsDataURL(selectedFile);
		}
	}

	type Clasificacion = {
		blanco_biologico: string;
		intensidad: 'slight' | 'moderate' | 'severe';
	};

	function clasificarResultados(resultados: [string, string]): Clasificacion {
		const blancoBiologicoMap: { [key: string]: string } = {
			botrytis: 'botrytis',
			oidio: 'oidio'
			// Agregar más mapeos según sea necesario
		};
		// console.log(resultados);
		const intensidadMap: { [key: string]: 'slight' | 'moderate' | 'severe' } = {
			slight: 'slight',
			moderate: 'moderate',
			severe: 'severe'
			// Agregar más mapeos según sea necesario
		};

		const blancoBiologico = resultados.find((result) => blancoBiologicoMap[result]);
		const intensidad = resultados.find((result) => intensidadMap[result]);

		const blancoBiologicoClasificado =
			blancoBiologico !== undefined ? blancoBiologicoMap[blancoBiologico] : '';
		const intensidadClasificada = intensidad !== undefined ? intensidadMap[intensidad] : 'slight';

		return {
			blanco_biologico: blancoBiologicoClasificado,
			intensidad: intensidadClasificada
		};
	}
</script>

{#await promise}
	<Loader />
{:then data}
	<div class="flex items-center justify-center w-2/3">
		<label
			for="dropzone-file"
			class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
		>
			<div class="flex flex-col items-center justify-center pt-5 pb-6">
				<svg
					class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
					aria-hidden="true"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 20 16"
				>
					<path
						stroke="currentColor"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
					/>
				</svg>
				<p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
					<span class="font-semibold">Click to upload</span> or drag and drop
				</p>
				<p class="text-xs text-gray-500 dark:text-gray-400">JPG or JPEG</p>
			</div>
			<input
				id="dropzone-file"
				type="file"
				class="hidden"
				accept=".jpg, .jpeg"
				on:change={handleFileSelect}
			/>
		</label>
	</div>
{/await}
