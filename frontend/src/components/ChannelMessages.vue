<template>
<section>
 <div class="message" v-for="message in messages">
  <div class="message-gutter">
   <img class="avatar" src="/img/slackatar.png" />
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
export default {
  name: 'channel-messages',
  data () {
    return {
      messages: [{
        username: 'shangxiao',
        time: '11:46pm',
        content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      }],
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
