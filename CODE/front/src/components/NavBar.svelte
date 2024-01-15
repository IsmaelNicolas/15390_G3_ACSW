<script lang="ts">
    import Moon from '../components/Moon.svelte'
	import Sun from '../components/Sun.svelte';
    import { goto } from '$app/navigation';
    import Logo from '$lib/images/new_logo.svg';

    function logout (){
        goto('/login');
    }

	function theme() {
		const icon1 = document.getElementById('moon');
		const icon2 = document.getElementById('sun');
		const html = document.querySelector('html');

		html?.classList.toggle('dark');
		if (icon1 && icon2) {
			icon1.classList.toggle('hidden');
			icon2.classList.toggle('hidden');
		}
	}
</script>

<nav class="bg-gray-100 border-gray-200 dark:bg-gray-900 mb-10">
	<div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
		<a href="/home" class="flex items-center space-x-3 rtl:space-x-reverse">
			<img src={Logo} class="h-14" alt="Logo" />
		</a>
		<div class="flex items-center  gap-2 md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
            <button
				type="button"
                on:click={theme}
				class="fill-gray-950 dark:fill-yellow-400"
			>
				<Sun />
				<Moon />
			</button>
			<button
				type="button"
                on:click={logout}
				class="h-fit text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800"
				>Salir</button
			>
			
		</div>
		<div
			class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1"
			id="navbar-cta"
		></div>
	</div>
</nav>
