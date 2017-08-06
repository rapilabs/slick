<template>
  <div id="app">
    <sidebar/>
    <channel/>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue';
import Channel from './components/Channel.vue';

export default {
  name: 'app',
  components: {
    Sidebar,
    Channel,
  },
};
</script>

<style>
 #app {
  display: flex;
 }
</style>
