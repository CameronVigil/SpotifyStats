<template>
  <div id="app">
  <b-container fluid>
    <b-row>
      <b-col class="col-3 px-2 column1 position-fixed">
        <h1>Spotify Stats</h1>
        <span>by Cameron Vigil</span>
        <div>
          <button  class="button" @click="scrollT">{{ TopTracks }}</button>
        </div>
      </b-col>
      <b-col cols="9" class="col offset-3 black-background">
      <h2 id="Top-Artists">Top Artists</h2>
        <h3>Last Month</h3>
          <span class="container" v-for="item in artistDataShort" :key="item.name">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
          </span>
        <h3>Last 6 Months</h3>
          <span class="container" v-for="item in artistDataMedium" :key="item.name">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
          </span>
        <h3>Overall</h3>
          <span class="container" v-for="item in artistDataLong" :key="item.name">
              <img :src="item.images[0].url" height="300px" width="300px">
              <div class="bottom-left">{{item.name}}</div>
          </span>
      <h2 id="Top-Tracks">Top Tracks</h2>
        <h3>Last 6 Months</h3>
          <span class="container" v-for="item in trackDataShort" :key="item.name">
                <img :src="item.album.images[0].url" height="300px" width="300px">
                <div class="bottom-left-track">
                  {{item.name}}
                </div>
                <div class="bottom-left-album">
                  {{item.album.artists[0].name}}
                </div>
            </span>
        <h3>Last 6 Months</h3>
          <span class="container" v-for="item in trackDataMedium" :key="item.name">
            <img :src="item.album.images[0].url" height="300px" width="300px">
            <div class="bottom-left-track">
              {{item.name}}
            </div>
            <div class="bottom-left-album">
              {{item.album.artists[0].name}}
            </div>
          </span>
        <h3>Overall</h3>
          <span class="container" v-for="item in trackDataLong" :key="item.name">
            <img :src="item.album.images[0].url" height="300px" width="300px">
            <div class="bottom-left-track">
              {{item.name}}
            </div>
            <div class="bottom-left-album">
              {{item.album.artists[0].name}}
            </div>
          </span>
      </b-col >
    </b-row>
  </b-container>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.17/vue.js"></script>
<script>
export default {
  name: 'app',
  data() {
    return {
      TopTracks: 'Top Tracks',
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
    scrollT() {
      const element = document.getElementById('Top-Tracks');
      element.scrollIntoView({ behavior: 'smooth' });
    },
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
    scroll() {
      const element = document.getElementById('Top-Artists');
      element.scrollIntoView({ behavior: 'smooth' });
    },
  },
  created() {
    this.getArtistShort();
    this.getArtistMedium();
    this.getArtistLong();
    this.getTrackShort();
    this.getTrackMedium();
    this.getTrackLong();
  },
};
</script>

<style>
#wrapper{
    width: 650px  ;
    height: auto;
    margin: 0 auto;
    margin-top: 100px;
    border-radius: 10px;
    color: white;
}
html,
body{
    margin: 0;
    padding: 0;
}
#app {
  font-family: 'Varela';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: rgb(45, 187, 45);
}
h1 {
  margin-top: 40px;
  font-weight:large;
  font-family: 'Varela';
  color: white;
}
h2 {
  font-family: 'Varela';
  margin-top: 40px;
  margin-bottom: 40px;
}
h3 {
  font-family: 'Varela';
  margin-top: 40px;
  margin-bottom: 40px;
  font-size: large;
}
span {
  font-family: 'Varela';
  padding: 0pt;
}
button{
  display: inline-block;
  position: relative;
  text-align: center;
  list-style: none;
  width: 377px;
  height: 40px;
  color: white;
  font-size: larger;
  font-family: 'Varela';
  background: transparent;
  border: none;
  max-width: fit-content;
}

/* Container holding the image and the text */
.container{
  position: relative;
  text-align: center;
  color: white;
  font-size: large;
  font-family: 'Varela';
  margin-left: 0;
}

img {
  mask-image: linear-gradient(to top, rgba(0,0,0,0) 0%,rgba(0,0,0,1) 100%);
  -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,.5) 0%,rgba(0,0,0,.99) 20%);
}
.black-background{
  background: black;
}
.column1{
  column-fill: auto;
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
.bottom-left-track {
  position: absolute;
  bottom: -120px;
  left: 16px;
  font-family: 'Varela';
  font-style: bold;
  font-size: medium;
}
.bottom-left-album {
  position: absolute;
  bottom: -140px;
  left: 16px;
  font-family: 'Varela';
  font-style: bold;
  font-size: medium;
}
/* Top left text */
.top-left {
  position: absolute;
  top: 8px;
  left: 16px;
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
