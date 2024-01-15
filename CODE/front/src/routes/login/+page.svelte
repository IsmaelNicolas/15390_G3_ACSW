<script>
	import Button from '../../components/Button.svelte';
	import InputForm from '../../components/InputForm.svelte';
	import Logo from '$lib/images/new_logo.svg';

	import { goto } from '$app/navigation';

	let username = '';
	let password = '';

	function handleLogin() {
		// Log the form elements to the console
		console.log('Username:', username);
		console.log('Password:', password);

		// You can use the form data for further processing
		// For example, make an API request with the login credentials

		// Redirect to the home page after handling the login
		goto('/home');
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

		<div class="md:border border-blue-500/50 md:h-80"></div>

		<div class="w-full sm:mx-auto sm:w-full sm:max-w-sm mt-4">
			<form on:submit|preventDefault={handleLogin} class="space-y-6 ">
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
