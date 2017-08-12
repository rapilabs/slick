<template>
 <nav>
  <header>
   <h1>Sliiick</h1>
   <div class="username">{{ user.username }}</div>
  </header>
  <section class="channels">
   <h2>Channels</h2>
   <ul>
    <li v-for="channel in channels">{{ channel }}</li>
   </ul>
  </section>
  <section class="direct-messages">
   <h2>Direct Message</h2>
   <ul>
    <li v-for="privmsg in privmsgs">{{ privmsg }}</li>
   </ul>
  </section>
 </nav>
</template>

<script>
export default {
  name: 'sidebar',
  props: ['user'],
  data () {
    return {
      channels: [
        'general',
        'random',
        'gifs',
      ],
      privmsgs: [
        'brntn',
        'veronica',
        'markush',
      ],
    };
  },
};
</script>

<style>
 nav {
  background-color: #4D394B;
  color: #AB9BA9;
  width: 220px;
  padding: 16px;
 }
 nav h1 {
  color: #fff;
 }
 nav header {
  height: 60px;
 }
 nav .username {
  font-size: .875rem;
 }
 nav h2 {
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: normal;
 }
 nav .channels, nav .direct-messages {
  margin: 8px 0 32px 0;
 }
 nav .channels li:before {
  content: '#';
  padding-right: 5px;
 }
 nav .direct-messages li:before {
  content: '○';
  padding-right: 5px;
 }
</style>
