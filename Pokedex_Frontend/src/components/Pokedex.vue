<template>
  <div id="parent">
    <div id="temp-box">
      <div id="pokedex-dot"></div>
      <div id="pokedex-dot-red"></div>
      <div id="pokedex-dot-yellow"></div>
      <div id="pokedex-dot-green"></div>
    </div>
    <div id="data-box">
      <h2 id="pokedex-header">POKEDEX RECORD:</h2>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
      <p>Lol</p>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style>
#parent {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

#temp-box {
  background-color: #fed2d3;
  border-radius: 5px 0 0 5px;
  height: 350px;
  border-left: 20px solid red;
  border-top: 50px solid red;
  border-right: 8px solid red;
  border-bottom: 30px solid red;
  width: 100%;
  position: "relative";
}

#pokedex-dot {
  height: 30px;
  width: 30px;
  background-color: cyan;
  border: 3px solid #fff;
  border-radius: 100px;
  position: "absolute";
  top: -40px;
  left: 0px;
}

#pokedex-dot-red {
  height: 10px;
  width: 10px;
  background-color: red;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -70px;
  left: 40px;
}

#pokedex-dot-yellow {
  height: 10px;
  width: 10px;
  background-color: yellow;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -80px;
  left: 55px;
}

#pokedex-dot-green {
  height: 10px;
  width: 10px;
  background-color: green;
  border: 1px solid black;
  border-radius: 100px;
  position: "absolute";
  top: -90px;
  left: 70px;
}

#data-box {
  background-color: red;
  padding: 0.5rem;
  border-radius: 0 5px 5px 0;
  height: 350px;
  width: 100%;
}

#pokedex-header {
  color: white;
  font-weight: "bold";
}
</style>
