<template>
  <div id="reg_block" class="modal-wrapper" v-if="showModal == 'register'">
    <div class="modal-window">
      <div id="personal_info">
        <div id="head_personal_info">
          <button id="cross_button">
            <img
              id="cross"
              :alt="cross"
              v-bind:src="'http://127.0.0.1:8000/static/cross.svg'"
              @click="hideModal()"
            />
          </button>
        </div>
        <h1 id="personal_info_name">Личные данные</h1>
        <div id="input_info">
          <label class="label" for="name"> Имя </label>
          <input class="input" type="text" id="firstname" />
        </div>
        <div id="input_info">
          <label class="label" for="phone"> Номер телефона </label>
          <input class="input" type="tel" id="phone_number" />
        </div>
        <div id="input_info">
          <label class="label" for="password"> Пароль </label>
          <input class="input" type="password" id="password" />
        </div>
      </div>
      <div id="address">
        <!-- <h1 id="personal_info_address">Адрес</h1>
        <div id="input_info">
          <label class="label" for="street"> Улица </label>
          <input class="input" type="text" id="street" />
        </div>
        <div id="input_info">
          <label class="label" for="house"> Дом </label>
          <input class="input" type="text" id="house" />
        </div>
        <div id="input_info">
          <label class="label" for="flat"> Квартира </label>
          <input class="input" type="text" id="flat" />
        </div> -->
        <div id="input_info">
          <label class="label" for="street"> Адрес </label>
          <input class="input" type="text" id="_address" />
        </div>
      </div>
      <div id="button_save">
        <button id="Choose" @click="regUser()">Сохранить</button>
      </div>
    </div>
    <div class="overlay"></div>
  </div>
</template>
<script>
import { request, gql } from "graphql-request";

var url = "http://127.0.0.1:8000/graphql";

export default {
  props: ["showModal"],
  methods: {
    regUser: function () {
      const firstname = document.getElementById("firstname").value;
      const username = document.getElementById("phone_number").value;
      const password = document.getElementById("password").value;
      const address = document.getElementById("_address").value;

      const reg_mutation = gql`
        mutation {
          register(firstname: "${firstname}", password: "${password}", username: "${username}", address: "${address}") {
            username
          }
        }
      `;

      request(url, reg_mutation).then((data) => {
        console.log("Data", data);
        alert(`Registerd user with username: ${data.register.username}`);
      });
      this.hideModal();
    },
    hideModal: function () {
      this.$emit("show", 0);
    },
  },
};
</script>

<style>
#reg_block {
  position: fixed;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  z-index: 100;
  width: 100%;
  height: 100%;
  top: 0%;
  background-color: #000000b3;
  align-items: center;
  cursor: all-scroll;
}

.modal-wrapper {
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
  background: #000000b3;
  z-index: 100;
}

.overlay {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.modal-window {
  width: 40%;
  height: fit-content;
  z-index: 2;
  background-color: #fff;
  border-radius: 15px;
  padding: 0 10px 0 10px;
}

#head_personal_info {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-content: space-between;
}

#personal_info_name {
  text-align: center;
  color: #be0000;
}

#personal_info_address {
  text-align: center;
  color: #be0000;
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
  padding-bottom: 15px;
}
.input {
  width: 100%;
  height: 10px;
  outline: none;
  border-radius: 15px;
  border: 2px solid #ff5757;
  background-color: #f8f8f8;
  font-size: 16px;
  color: #70544f;
  transition: background-color 0.35s;
  height: 40px;
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

#button_save {
  width: 100%;
  padding: 12px 0px 12px 0px;
  align-self: space-between;
}

#reg_link {
  color: #0084fe;
  opacity: 68%;
  align-self: flex-start;
  padding: 12px 16px 12px 0px;
  cursor: pointer;
}
</style>