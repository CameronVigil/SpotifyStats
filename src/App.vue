<template>
  <div id="app">
  <b-container fluid>
    <b-row>
      <b-col>
        <h1>Spotify Stats</h1>
        <span>by Cameron Vigil</span>
      </b-col>
      <b-col cols="9">
      <h2>{{tartists}}</h2>
        <h3>Last Month</h3>
          <span v-for="item in artistDataShort" :key="item.name">
            <span class="container">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
            </span>
          </span>
        <h3>Last 6 Months</h3>
          <span v-for="item in artistDataMedium" :key="item.name">
            <span class="container">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
            </span>
          </span>
        <h3>Overall</h3>
          <span v-for="item in artistDataLong" :key="item.name">
            <span class="container">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
            </span>
          </span>
      </b-col >
    </b-row>
  </b-container>
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
      albumDataShort: [],
      albumDataMedium: [],
      albumDataLong: [],
      trackDataShort: [],
      trackDataMedium: [],
      trackDataLong: [],
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
    getAlbumShort() {
      fetch('album_short.json')
        .then((response) => response.json())
        .then((data) => { this.albumDataShort = data; });
    },
    getAlbumMedium() {
      fetch('album_medium.json')
        .then((response) => response.json())
        .then((data) => { this.albumDataMedium = data; });
    },
    getAlbumLong() {
      fetch('album_long.json')
        .then((response) => response.json())
        .then((data) => { this.albumDataLong = data; });
    },
    getTrackShort() {
      fetch('track_short.json')
        .then((response) => response.json())
        .then((data) => { this.trackDataShort = data; });
    },
    getTrackMedium() {
      fetch('track_medium.json')
        .then((response) => response.json())
        .then((data) => { this.trackDataMedium = data; });
    },
    getTrackLong() {
      fetch('track_long.json')
        .then((response) => response.json())
        .then((data) => { this.trackDataLong = data; });
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
h3 {
  margin-top: 40px;
  margin-bottom: 40px;
  background: rgb(45, 151, 45);
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
my-span{
  color:white;
  font-weight: bold;
  float: left;
}
/* Container holding the image and the text */
.container{
  position: relative;
  text-align: center;
  color: white;
  font-size: large;
}

/* Bottom left text */
.bottom-left {
  position: absolute;
  bottom: -140px;
  left: 16px;
  font-family: 'Varela';
  font-style: bold;
  font-size: larger;
}

/* Top left text */
.top-left {
  position: absolute;
  top: 8px;
  left: 16px;
}

/* Top right text */
.top-right {
  position: absolute;
  top: 8px;
  right: 16px;
}

/* Bottom right text */
.bottom-right {
  position: absolute;
  bottom: 8px;
  right: 16px;
}

/* Centered text */
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

@font-face {
  font-family: "BebasKai";
  src: local("BebasKai"),   url(fonts/bebas-kai/BebasKai.ttf) format("truetype");
}

@font-face {
  font-family: "Varela";
  src: local("Varela"), url(fonts/varela/varela.regular.ttf) format("truetype");
}

</style>
