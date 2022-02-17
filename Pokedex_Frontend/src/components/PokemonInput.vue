<template>
  <div>
    <input
      v-model="pokemonId"
      placeholder="Search for a Pokemon by it's ID"
      type="number"
      v-on:keyup.enter="passId"
      :class="['pokemon-input', { 'pokemon-input-error': lastPokemon }]"
    />
    <button
      :disabled="lastPokemon === true"
      v-on:click="passId"
      :class="{
        'search-button': !lastPokemon,
        'search-button-disabled': lastPokemon,
      }"
    >
      GO!
    </button>
    <p v-if="lastPokemon" class="error-text">
      There is no Pokemon with ID larger than 809!
    </p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      pokemonId: "",
      lastPokemon: false,
    };
  },
  emits: ["sendSearchId"],
  methods: {
    passId() {
      console.log("LOL");
      this.$emit("sendSearchId", this.pokemonId);
    },
  },
  watch: {
    pokemonId(newPokemonID) {
      if (newPokemonID > 809) {
        this.lastPokemon = true;
      } else {
        this.lastPokemon = false;
      }
    },
  },
};
</script>
<style>
.pokemon-input {
  text-align: center;
  margin-top: 1em;
  width: 85%;
  height: 40px;
  color: #1b5eac;
  font-size: 1.5em;
  font-weight: bold;
  border: 3px solid #1b5eac;
  border-radius: 5px 0 0 5px;
  background: #eee;
}

.pokemon-input-error {
  color: red;
  border: 3px solid red;
}

.search-button {
  width: 15%;
  height: 40px;
  font-size: 1.5em;
  font-weight: bold;
  color: white;
  background: #1b5eac;
  border: 3px solid #1b5eac;
  border-radius: 0 5px 5px 0;
  transition: transform 0.2s;
}

.search-button:hover {
  transform: scale(1.05);
  cursor: pointer;
}

.search-button-disabled {
  width: 15%;
  height: 40px;
  font-size: 1.5em;
  font-weight: bold;
  color: white;
  cursor: not-allowed;
  opacity: 0.8;
  background: grey;
  border: 3px solid grey;
  border-radius: 0 5px 5px 0;
}

.error-text {
  color: red;
  font-weight: bold;
  text-align: center;
  width: 90%;
}
</style>
