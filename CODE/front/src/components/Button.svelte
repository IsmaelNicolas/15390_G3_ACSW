<script lang="ts">
    export let id: string;
    export let type: "submit" | "button" = "button";
    export let text = "";
  </script>

<div>
    <button
        id={id}  
        type={type}
        class="w-full bg-blue-500 shadow-lg shadow-blue-500/70 py-1.5 px-2.5 mx-auto rounded-md border-1 text-white dark:bg-transparent dark:border-2 dark:border-blue-500 dark:shadow-blue-800/50"
    >{text}</button>
</div>
