<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h2>by Cameron Vigil</h2>
    <ul>
      <li>{{tartists}}</li>
      <li>{{ttracks}}</li>
      <li>{{talbums}}</li>
    </ul>

      <ul></ul>
      <ul></ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data() {
    return {
      msg: 'Spotify Stats',
      title: 'Spotify Stats',
      ttracks: 'Top Tracks',
      tartists: 'Top Artists',
      talbums: 'Top Albums',
    };
  },
  methods: {
    method() {
      axios.get("/main.py")
      
    
    },
  },
};
</script>

<style>
#wrapper{
    width: 650px  ;
    height: auto;
    background-color: rgb(198, 241, 200);
    margin: 0 auto;
    margin-top: 200px;
    border-radius: 10px;
}
html,
body{
    margin: 0;
    padding: 0;
    background-color:rgb(250, 28, 65);
}
#app {
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:cadetblue;
  margin-top: 40px;
  background:black;
  background-color: black;
}

h1 {
  font-weight:large;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}

h2{
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
  color: whitesmoke;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
