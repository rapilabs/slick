<template>
<div class="channel">
 <channel-header />
 <channel-messages />
 <channel-footer />
</div>
</template>

<script>
import ChannelHeader from './ChannelHeader.vue';
import ChannelMessages from './ChannelMessages.vue';
import ChannelFooter from './ChannelFooter.vue';

export default {
  name: 'channel',
  components: {
    ChannelHeader,
    ChannelMessages,
    ChannelFooter,
  },
};
</script>

<style>
.channel {
 flex: 1;
 display: flex;
 flex-direction: column;
}
</style>
