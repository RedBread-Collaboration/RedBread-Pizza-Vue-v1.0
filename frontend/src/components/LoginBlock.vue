<template>
  <div id="log_block" v-if="showModal == 'login'">
    <div id="header_login">
      <div id="enter_span">
        <h1>Вход на сайт</h1>
      </div>
      <button id="cross_button">
        <img
          id="cross"
          :alt="cross"
          v-bind:src="'http://127.0.0.1:8000/static/cross.svg'"
          @click="hideModal()"
        />
      </button>
    </div>
    <div id="center_block">
      <div id="input_info">
        <label class="label" for="phone-number"> Номер телефона </label>
        <input class="input" type="tell" id="phone_number" />
      </div>
      <div id="input_info">
        <label class="label" for="username">Пароль</label>
        <input class="input" type="password" id="password" />
      </div>
      <div id="button_login">
        <button id="Choose" type="button" @click="authorize()">Войти</button>
        <a id="reg_link" @click="showModalWin()">
          <span>Регистрация</span>
        </a>
      </div>
    </div>
  </div>
</template>
<script>
import { request, gql } from "graphql-request";
import cookies from "vue-cookies";

var url = "http://127.0.0.1:8000/graphql";

export default {
  props: ["showModal"],
  data() {
    return {};
  },
  methods: {
    authorize() {
      const username = document.getElementById("phone_number").value;
      const password = document.getElementById("password").value;
      console.log("username", username);
      console.log("password", password);

      const authorize_query = gql`
        mutation {
          login(password: "${username}", username: "${password}")
        }
      `;
      request(url, authorize_query).then((data) => {
        console.log("New token", data.login)
        cookies.set("_token", data.login, "1h");
      });
      this.hideModal();
    },
    hideModal: function () {
      this.$emit("show", 0);
    },
    showModalWin: function () {
      this.$emit("show", "register");
    },
  },
};
</script>
<style scoped>
#log_block {
  position: absolute;
  top: 10%;
  right: 0%;
  width: 300px;
  box-shadow: 16px 16px 16px #00000040;
  border-radius: 15px;
  background-color: #fff;
  margin: 5px;
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
  z-index: 100;
  overflow-x: hidden;
}
#header_login {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: space-between;
}
#cross_button {
  border: none;
  background: none;
  width: 20%;
  margin-right: -5%;
  margin-top: 1%;
}
#cross {
  width: 40%;
  align-self: center;
  height: auto;
  border: none;
  cursor: pointer;
}

#enter_span {
  font-size: 100%;
  font-weight: 700;
  padding-top: 15px;
  padding-left: 10px;
  padding-bottom: 10px;
}
#input_info {
  display: flex;
  flex-direction: column;
  height: fit-content;
  padding: 5px;
}
.input {
  width: 100%;
  height: 10px;
  outline: none;
  padding: 12px 16px 12px 0px;
  border-radius: 15px;
  border: 2px solid #ff5757;
  background-color: #f8f8f8;
  font-size: 16px;
  color: #70544f;
  transition: background-color 0.35s;
}

.label {
  font-size: 80%;
  opacity: 70%;
}

#center_block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: fit-content;
}

#Choose {
  width: 100%;
  height: 40px;
  background-color: #ff5757;
  border: none;
  border-radius: 40px;
  color: #fff;
  font-family: "Roboto";
  font-size: 100%;
  font-weight: 700;
  cursor: pointer;
}

#button_login {
  width: 78%;
  padding: 12px 0px 12px 15px;
  align-self: space-between;
}

#reg_link {
  color: #0084fe;
  opacity: 68%;
  align-self: flex-start;
  padding: 12px 16px 12px 0px;
}
</style>