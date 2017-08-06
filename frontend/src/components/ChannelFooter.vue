<template>
<footer>
 <form class="message-form">
  <input type="text" v-bind:placeholder="msgPlaceholder" />
  <button class="emoji">&#x1F600;</button>
 </form>
</footer>
</template>

<script>
export default {
  name: 'channel-footer',
  data () {
    let channelName = 'general';
    return {
      msgPlaceholder: `Message #${channelName}`,
    };
  },
};
</script>

<style>
.channel > footer {
 padding-left: 20px;
 padding-right: 20px;
 padding-bottom: 20px;
}
.message-form {
 display: flex;
 border: 2px solid rgba(160,160,162,.7);
 border-radius: 0.375rem;
 height: 40px;
 padding-left: 10px;
 padding-right: 10px;
}
.message-form input {
 flex: 1;
 font-weight: 300;
}
.message-form input::-webkit-input-placeholder {
 color: #a0a0a0;
}
.message-form button {
 font-size: 18px;
 color: white;
 -webkit-text-stroke-width: 1px;
 -webkit-text-stroke-color: #adadad;
}
.message-form input, .message-form button {
 border: none;
 background: none;
}
</style>
