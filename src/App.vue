<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h2>by Cameron Vigil</h2>
      <div>{{tartists}}</div>
        <button v-on:click="getArtistData">Artists Data</button>
      <div>{{artistDataList}}</div>

      <div>{{ttracks}}</div>
        <button v-on:click="getTrackData">Track Data</button>
      <div>{{trackDataList}}</div>

      <div>{{talbums}}</div>
        <button v-on:click="getAlbumData">Album Data</button>
      <div>{{lbumDataList}}</div>

  </div>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'app',
  data() {
    return {
      msg: 'Spotify Stats',
      title: 'Spotify Stats',
      ttracks: 'Top Tracks',
      tartists: 'Top Artists',
      talbums: 'Top Albums',
      artistDataList: [],
      albumDataList: [],
      trackDataList: [],
    };
  },
  methods: {
    getArtistData() {
      fetch('artist.json')
        .then((response) => response.json())
        .then((data) => { this.artistDataList = data; });
    },
    getAlbumData() {
      fetch('album.json')
        .then((response) => response.json())
        .then((data) => { this.albumDataList = data; });
    },
    getTrackData() {
      fetch('track.json')
        .then((response) => response.json())
        .then((data) => { this.trackDataList = data; });
    },
  },
};
</script>

<style>
#wrapper{
    width: 650px  ;
    height: auto;
    background-color: black;
    margin: 0 auto;
    margin-top: 200px;
    border-radius: 10px;
    color: white;
}
html,
body{
    margin: 0;
    padding: 0;
    color: white;
    background-color:black;
}
#app {
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 40px;
  background: black;
}

h1 {
  font-weight:large;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  color: white;
}

h2{
  font-weight: normal;
  color: white;
}

button{
  display: inline-block;
  list-style: none;
  margin: 0 10px;
  color: rgb(24, 59, 136);
}
</style>
