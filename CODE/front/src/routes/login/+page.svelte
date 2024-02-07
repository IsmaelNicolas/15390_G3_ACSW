<script>
	import Button from '../../components/Button.svelte';
	import InputForm from '../../components/InputForm.svelte';
	import Logo from '$lib/images/new_logo.svg';
	import {API,setCookie} from '../../Utils/function'
	import { goto } from '$app/navigation';
	import {notifications} from '../../Utils/notification'
	import Toast from '../../components/Toast.svelte'

	let username = '';
	let password = '';

	async function handleLogin() {
		const formData = new FormData();
		formData.append('username', username);
		formData.append('password', password);

		try {
			const response = await fetch(API + '/login', {
				method: 'POST',
				body: formData,
				credentials: 'include'
			});

			// console.log(response);

			if (response.ok) {
				const { access_token } = await response.json();
				setCookie("access_token",access_token,7,'/');
				goto('/home');
			} else {
				notifications.danger('Credenciales incorrectas', 500)
				alert("Credenciales incorrectas")
				console.log('Error in response:', await response.text());
			}
		} catch (error) {
			notifications.danger('STOP NOW!', 500)
			console.error('Error durante fetch:', error);
		}
	}
</script>

<svelte:head>
	<title>Login</title>
	<meta name="Login" content="Clasificador de plagas" />
</svelte:head>

<div class="flex items-center justify-center h-screen dark:bg-gray-900">
	<div class="flex flex-col md:flex-row items-center justify-around w-4/5">
		<div class="sm:mx-auto sm:w-full sm:max-w-sm">
			<img class="mx-auto h-auto w-auto" src={Logo} alt="Your Company" />
		</div>

		<div class="w-full sm:mx-auto sm:w-full sm:max-w-sm mt-4">
			<form on:submit|preventDefault={handleLogin} class="space-y-6">
				<InputForm
					bind:value={username}
					id="username"
					label="Usuario"
					type="text"
					placeholder="Nombre de usuario"
					classProp="mb-5 w-full"
				/>
				<InputForm
					bind:value={password}
					id="password"
					label="Contraseña"
					type="password"
					placeholder="Contraseña"
				/>
				<br />
				<Button id="btnlogin" text="Iniciar Sesión" type="submit" />
			</form>
		</div>
	</div>
</div>
