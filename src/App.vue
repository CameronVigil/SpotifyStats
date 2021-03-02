<template>
  <div id="app">
    <h1>{{ msg }}</h1><span>by Cameron Vigil</span>
      <h3>{{tartists}}</h3>
        <h4>Last Month</h4>
          <span v-for="item in artistDataShort" :key="item.name">{{item.name+ "   "}}</span>
        <h4>Last 6 Months</h4>
          <span v-for="item in artistDataMedium" :key="item.name">{{item.name+ "   "}}</span>
        <h4>Overall</h4>
          <span v-for="item in artistDataLong" :key="item.name">{{item.name+ "   "}}</span>
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
      artistDataShort: [],
      artistDataMedium: [],
      artistDataLong: [],
      albumDataList: [],
      trackDataList: [],
    };
  },
  methods: {
    getArtistShort() {
      fetch('artist_short.json')
        .then((response) => response.json())
        .then((data) => { this.artistDataShort = data; });
    },
    getArtistMedium() {
      fetch('artist_medium.json')
        .then((response) => response.json())
        .then((data) => { this.artistDataMedium = data; });
    },
    getArtistLong() {
      fetch('artist_long.json')
        .then((response) => response.json())
        .then((data) => { this.artistDataLong = data; });
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
  created() {
    this.getArtistShort();
    this.getArtistMedium();
    this.getArtistLong();
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
  font-family: Impact, 'Arial Narrow Bold', sans-serif;
  color: white;
}
span {
  font-family:Verdana, Geneva, Tahoma, sans-serif
}
button{
  display: inline-block;
  list-style: none;
  margin: 0 10px;
  color: rgb(24, 59, 136);
}
</style>
