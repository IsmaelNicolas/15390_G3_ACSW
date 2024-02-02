<script lang="ts">
    export let id: string;
    export let label: string;
    export let placeholder: string = "";
    export let type: "number" | "text" | "password" | "email" = "text";
    export let classProp: string = "";
    export let value: string = "";
</script>

<div class="{classProp}">
    <label for={id} class="block text-sm font-medium leading-6 text-gray-900 dark:text-white">
        {label}
    </label>
    <div class="mt-2">
        {#if type === 'text'}
            <input
                bind:value={value}
                id={id}
                name="email"
                type="text"
                autocomplete={'user'}
                placeholder={placeholder}
                required
                class="w-full py-3 px-2.5 rounded-xl border-1 shadow-lg shadow-gray-300 dark:shadow-gray-500/20 placeholder:text-gray-400 dark:bg-gray-900 dark:text-white"
            />
        {:else if type === 'password'}
            <input
                bind:value={value}
                id={id}
                name="email"
                type="password"
                autocomplete={'user'}
                placeholder={placeholder}
                required
                class="w-full py-3 px-2.5 rounded-xl border-1 shadow-lg shadow-gray-300 dark:shadow-gray-500/20 placeholder:text-gray-400 dark:bg-gray-900 dark:text-white"
            />
        {:else if type === 'email'}
            <input
                bind:value={value}
                id={id}
                name="email"
                type="email"
                autocomplete={'email'}
                placeholder={placeholder}
                required
                class="w-full py-3 px-2.5 rounded-xl border-1 shadow-lg shadow-gray-300 dark:shadow-gray-50/20 placeholder:text-gray-400 dark:bg-gray-900 dark:text-white"
            />
        {:else if type === 'number'}
            <input
                bind:value={value}
                id={id}
                min="0"
                name="email"
                type="number"
                autocomplete={'user'}
                placeholder={placeholder}
                required
                class="w-full py-3 px-2.5 rounded-xl border-1 shadow-lg shadow-gray-300 dark:shadow-gray-50/20 placeholder:text-gray-400 dark:bg-gray-900 dark:text-white"
            />
        {/if}
    </div>
</div>
