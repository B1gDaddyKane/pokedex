<template>
  <div class="pokedex-container">
    <img
      src="@/assets/images/pokemon_logo.jpg"
      alt="Pokemon Logo"
      id="pokemon-logo"
    />
    <h1 class="fake-pokemon-h1">"Husk at bruge den rigtige extension!"</h1>
    <p class="fake-pokemon-paragraph">...ellers går det galt</p>
    <p class="text-right">Jens Jensen 2022</p>
    <div style="margin-top: 2rem">
      <Pokedex :pokemon="getResult" />
      <PokemonInput @sendSearchId="searchForPokemon" />
      <p class="loading-text" v-if="loading">Fetching your Pokemon...</p>
    </div>
  </div>
</template>

<script>
import PokemonInput from "../components/PokemonInput.vue";
import Pokedex from "../components/Pokedex.vue";
export default {
  data() {
    return {
      getResult: null,
      loading: false,
    };
  },
  components: { PokemonInput, Pokedex },
  methods: {
    formatResponse(res) {
      return JSON.stringify(res, null, 2);
    },
    async searchForPokemon(pokemonIdEvent) {
      this.loading = true;
      console.log(pokemonIdEvent);
      if (pokemonIdEvent) {
        try {
          const res = await fetch(
            `http://localhost:5000/pokemon/${pokemonIdEvent}`
          );
          if (!res.ok) {
            const message = `An error has occured: ${res.status} - ${res.statusText}`;
            this.loading = false;
            throw new Error(message);
          }
          const data = await res.json();
          const result = {
            data: data,
            status: res.status,
            statusText: res.statusText,
            headers: {
              "Content-Type": res.headers.get("Content-Type"),
              "Content-Length": res.headers.get("Content-Length"),
            },
          };
          this.getResult = result;
          this.loading = false;
        } catch (err) {
          this.loading = false;
          this.getResult = err.message;
        }
      }
    },
  },
};
</script>

<style>
.pokedex-container {
  background-color: #ffcc01;
  height: 100vh;
  padding: 0rem 2rem 1rem 2rem;
}

#pokemon-logo {
  height: auto;
  width: 100%;
  animation: pulse 3s linear infinite;
}

.loading-text {
  text-align: center;
  font-weight: bold;
  color: #1b5eac;
}

.fake-pokemon-h1 {
  -webkit-text-stroke: 0.1rem #1b5eac;
  color: #ffcc01;
  font-weight: bold;
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
}

.fake-pokemon-paragraph {
  -webkit-text-stroke: 0.08rem #1b5eac;
  font-size: medium;
  color: #ffcc01;
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
}

.text-right {
  font-size: smaller;
  font-weight: bold;
  color: #1b5eac;
  float: right;
  font-style: italic;
}

@keyframes pulse {
  0% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
  50% {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }
  100% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes slide {
  0% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
  50% {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }
  100% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
</style>
