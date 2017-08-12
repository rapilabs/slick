<template>
<section>
 <div class="message" v-for="message in messages">
  <div class="message-gutter">
   <img class="avatar" v-bind:src="'/avatar?username=' + message.username" width="48" height="48" />
  </div>
  <div class="message-content">
   <div class="message-info">
    <span class="message-sender">{{ message.username }}</span>
    <span class="message-time">{{ message.time }}</span>
   </div>
   <div class="message-body">{{ message.content }}</div>
  </div>
 </div>
</section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'channel-messages',
  mounted () {

    let protocol = window.location.protocol === 'https:' ? 'wss' : 'ws';
    let ws = new WebSocket(`${protocol}://${window.location.host}/sub`)
    ws.onopen = () => {
      console.log('Connected…');
    };
    ws.onmessage = event => {
      this.messages.push(JSON.parse(event.data));
    };

    axios.get('/messages')
      .then(response => {
        this.messages = response.data;
      });
  },
  data () {
    return {
      messages: [],
    };
  },
};
</script>

<style>
.channel > section {
 flex: 1;
}
.message {
 display: flex;
}
.message-gutter {
 flex-basis: 62px;
 flex-grow: 0;
 flex-shrink: 0;
 text-align: right;
 margin-right: 10px;
}
.avatar {
 border-radius: 0.2rem;
}
.message-sender {
 font-weight: bold;
 margin-right: 5px;
}
.message-time {
 color: #9e9ea6;
 font-size: 12px;
}
.message-content {
 font-size: 15px;
 line-height: 22px;
}
</style>
