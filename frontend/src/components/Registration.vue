<template>
 <div id="registration">
  <h1>Who are you?</h1>
  <p v-if="isError" class="error">{{errorMsg}}</p>
  <form v-on:submit="handleSubmit">
   <input placeholder="Enter a username!" v-model="username" />
  </form>
 </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'registration',
  data() {
    return {
      username: '',
      isError: false,
      errorMsg: '',
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      if (this.username === '') {
        this.isError = true;
        this.errorMsg = 'Please enter a username';
        return;
      }
      this.isError = false;
      this.errorMsg = '';
      axios.post('/register', {
        username: this.username,
      }).then(() => {
        this.$emit('registered', {
          username: this.username,
        });
      }).catch(error => {
        if (error.response.status == 400) {
          this.isError = true;
          this.errorMsg = error.response.data;
        }
      });
        
    },
  },
};
</script>

<style>
#registration {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

#registration .error {
  color: firebrick;
}

#registration form {
  margin-top: 1em;
}
</style>
