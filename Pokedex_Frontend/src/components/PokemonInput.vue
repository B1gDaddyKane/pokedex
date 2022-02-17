<template>
  <div>
    <input
      v-model="pokemonId"
      placeholder="Search for a Pokemon by it's ID"
      type="number"
      :class="{ 'pokemon-input': !idTooLong, 'pokemon-input-error': idTooLong }"
    />
    <button
      :disabled="idTooLong === true"
      v-on:click="passId"
      :class="{
        'search-button': !idTooLong,
        'search-button-disabled': idTooLong,
      }"
    >
      GO!
    </button>
    <p v-if="idTooLong" class="error-text">
      There is no Pokemon ID with more than 3 characters!
    </p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      pokemonId: "",
      idTooLong: false,
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
      if (newPokemonID.toString().length > 3) {
        this.idTooLong = true;
      } else this.idTooLong = false;
    },
  },
};
</script>
<style>
.pokemon-input {
  text-align: center;
  margin-top: 1rem;
  height: 40px;
  width: 90%;
  border: 3px solid #1b5eac;
  border-radius: 5px 0 0 5px;
  background: #eee;
}

.pokemon-input-error {
  font-weight: bold;
  text-align: center;
  margin-top: 1rem;
  height: 40px;
  width: 90%;
  border: 3px solid red;
  border-radius: 5px 0 0 5px;
  background: #eee;
  color: red;
}

.search-button {
  height: 40px;
  width: 10%;
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
  height: 40px;
  width: 10%;
  font-weight: bold;
  color: white;
  cursor: not-allowed;
  opacity: 0.8;
  background: red;
  border: 3px solid red;
  border-radius: 0 5px 5px 0;
}

.error-text {
  color: red;
  font-weight: bold;
  text-align: center;
  width: 90%;
}
</style>
