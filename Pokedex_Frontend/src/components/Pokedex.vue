<template>
  <div class="parent">
    <div class="temp-box">
      <div class="pokedex-dot"></div>
      <div class="pokedex-dot-red"></div>
      <div class="pokedex-dot-yellow"></div>
      <div class="pokedex-dot-green"></div>
    </div>
    <div class="data-box">
      <h1 class="pokedex-header">POKEDEX RECORD:</h1>
      <h2 class="pokemon-name">
        {{
          this.pokemon
            ? "#" +
              this.pokemon["data"]["pokeID"] +
              " " +
              this.pokemon["data"]["pokename"]
            : "Pokemon"
        }}
      </h2>
      <div v-if="this.pokemon" class="type-container">
        <p
          :class="['type', this.pokemon['data']['type'][0]?.toLowerCase()]"
          style="margin-right: 0.5em"
        >
          {{ this.pokemon ? this.pokemon["data"]["type"][0] : "Primary Type" }}
        </p>
        <p
          v-if="this.pokemon['data']['type'][1]"
          :class="['type', this.pokemon['data']['type'][1]?.toLowerCase()]"
        >
          {{ this.pokemon["data"]["type"][1] }}
        </p>
      </div>
      <div v-if="this.pokemon" class="stats-container">
        <p>
          HP:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["HP"] : "" }}</span
          >
        </p>
        <p>
          Attack:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["Attack"] : "" }}</span
          >
        </p>
        <p>
          Defense:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["Defense"] : "" }}</span
          >
        </p>
        <p>
          Sp. Attack:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["Sp. Attack"] : "" }}</span
          >
        </p>
        <p>
          Sp. Defense:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["Sp. Defense"] : "" }}</span
          >
        </p>
        <p>
          Speed:
          <span style="font-weight: bold">
            {{ this.pokemon ? this.pokemon["data"]["Speed"] : "" }}</span
          >
        </p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    pokemon: JSON,
  },
};
</script>
<style>
.parent {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.temp-box {
  background-color: #fed2d3;
  border-radius: 10px 0 0 10px;
  height: 350px;
  border-left: 20px solid red;
  border-top: 50px solid red;
  border-right: 8px solid red;
  border-bottom: 30px solid red;
  width: 100%;
  position: "relative";
}

.pokedex-dot {
  height: 30px;
  width: 30px;
  background-color: cyan;
  border: 3px solid #fff;
  border-radius: 100px;
  position: "absolute";
  top: -40px;
  left: 0px;
}

.pokedex-dot-red {
  height: 10px;
  width: 10px;
  background-color: red;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -70px;
  left: 40px;
}

.pokedex-dot-yellow {
  height: 10px;
  width: 10px;
  background-color: yellow;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -80px;
  left: 55px;
}

.pokedex-dot-green {
  height: 10px;
  width: 10px;
  background-color: green;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -90px;
  left: 70px;
}

.data-box {
  background-color: red;
  padding: 0.5em;
  border-radius: 0 10px 10px 0;
  height: 350px;
  width: 100%;
}

.pokedex-header {
  margin-top: -0.2em;
  color: white;
  font-weight: "bold";
}

.pokemon-name {
  margin-top: 0.5em;
  color: white;
  font-weight: bold;
}

.type-container {
  display: flex;
}

.type {
  font-weight: bold;
  border: 1px solid black;
  padding: 0 1em;
  border-radius: 8px;
  color: white;
}

.fire {
  background: #f07f2f;
}

.flying {
  background: #a890f0;
  color: black;
}

.grass {
  background: #7ac74a;
}

.poison {
  background: #a040a1;
}

.water {
  background: #7190db;
}

.bug {
  background: #a8b821;
}

.normal {
  background: #a9a878;
  color: black;
}

.electric {
  background: #f9d030;
  color: black;
}

.ground {
  background: #e0c069;
  color: black;
}

.fairy {
  background: #f1b6bc;
  color: black;
}

.fighting {
  background: #c12f28;
}

.rock {
  background: #b59f41;
}

.ghost {
  background: #705798;
}

.steel {
  background: #b9b9cb;
  color: black;
}

.psychic {
  background: #f85888;
  color: black;
}

.ice {
  background: #98d8d8;
  color: black;
}

.dragon {
  background: #6f3bef;
}

.dark {
  background: #6f5848;
}

.stats-container {
  font-weight: bold;
  margin-top: 2em;
  color: white;
}
</style>
