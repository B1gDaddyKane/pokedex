<template>
  <div>
    <input
      id="pokemon-input"
      v-model="pokemonId"
      placeholder="Search for a Pokemon by it's ID"
      type="number"
    />
  </div>
</template>
<script>
export default {
  data() {
    return {
      pokemonId: "",
      count: 0,
    };
  },
  watch: {
    pokemonId(newPokemonID) {
      console.log("Searching for Pokemon with ID: " + newPokemonID);
    },
  },
};
</script>
<style>
#pokemon-input {
  margin-top: 1rem;
  height: 40px;
  width: 100%;
  border: 3px solid #1b5eac;
  border-radius: 5px;
  padding-left: 5px;
  background-color: #eee;
}
</style>
