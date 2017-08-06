<template>
<header>
 <div>
  <h2>#{{ channelName }}</h2>
  <div class="header-info">
   <span class="user-count"><span class="emoji">&#x1f464;</span> {{ numUsersOnline }}</span>
   <span class="separator">|</span>
   <span class="topic">{{ topic }}</span>
  </div>
 </div>
 <div>
  <form class="search-form">
   <button class="emoji">&#x1F50D;</button>
   <input type="text" placeholder="Search" />
   <button>&#x24e7;</button>
  </form>
 </div>
</header>
</template>

<script>
export default {
  name: 'channel-header',
  data () {
    return {
      channelName: 'general',
      numUsersOnline: 21,
      topic: 'melbdjango',
    };
  },
};
</script>

<style>
.channel > header {
 border-bottom: 1px solid #E8E8E8;
 padding: 10px 20px;
 display: flex;
 justify-content: space-between;
}
.channel h2 {
 font-size: 1.125rem;
 font-weight: 900;
}
.header-info {
 color: #717274;
 font-size: 0.8125rem;
 font-weight: 300;
 margin-top: 5px;
}
.separator {
 margin-left: 0.4rem;
 margin-right: 0.4rem;
}
.search-form {
 border: 1px solid rgba(113,114,116,.5);
 border-radius: 0.35rem;
 width: 227px;
 height: 34px;
 display: flex;
 align-items: center;
}
.search-form input {
 flex: 1;
 color: rgb(85, 84, 89);
}
.search-form button {
 color: #9e9ea6;
}
.search-form input, .search-form button {
 border: none;
 background: none;
 font-size: 15px;
 font-weight: 300;
}
</style>
