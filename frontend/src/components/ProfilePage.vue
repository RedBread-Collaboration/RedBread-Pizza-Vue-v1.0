<template>
  <div
    id="reg_block"
    class="modal-wrapper md-effect-1"
    v-if="showModal == 'profile'"
  >
    <div class="modal-window md-content">
      <div id="personal_info">
        <div id="head_personal_info">
          <button id="cross_button">
            <img
              id="cross"
              :alt="cross"
              v-bind:src="'http://127.0.0.1:8000/static/cross.svg'"
              @click="this.hideModal()"
            />
          </button>
        </div>
        <h1 id="personal_info_name">Личные данные</h1>
        <div id="input_info">
          <label class="label" for="name"> Имя </label>
          <input
            class="input"
            type="text"
            :value="user_data.firstname"
            id="firstname"
          />
        </div>
        <div id="input_info">
          <label class="label" for="phone"> Номер телефона </label>
          <!-- <input
            class="input"
            type="tel"
            :value="user_data.username"
            id="phone_number"
          /> -->
          <label class="input" for="phone"> {{ user_data.username }} </label>
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
          <input
            class="input"
            type="text"
            :value="user_data.address"
            id="_address"
          />
        </div>
        <div id="input_info">
          <label class="label" for="street"> Права администратора {{user_data.is_superuser}}</label>
          <input
            class="input"
            type="checkbox"
            :checked="user_data.is_superuser"
            id="is_superuser"
          />
        </div>
      </div>
      <div id="button_save">
        <button id="Choose" @click="updateUser()">Сохранить</button>
      </div>
    </div>
    <div class="overlay"></div>
  </div>
</template>
<script>
import { request, gql } from "graphql-request";
import { v4 as uuid4 } from "uuid";
import cookies from "vue-cookies";

var _token = cookies.get("_token");
var _session_id = cookies.get("_Session_ID");

if (_token) {
  console.log("Token found in cookie: ", _token);
} else {
  _token = "";
}

if (_session_id) {
  console.log("Session_ID found in cookie: ", _session_id);
} else {
  _session_id = uuid4();
  cookies.set("_Session_ID", _session_id, "1h");
}

var url = "http://127.0.0.1:8000/graphql";

export default {
  props: ["showModal"],
  data() {
    return {
      user_data: this.getUser(),
    };
  },
  methods: {
    updateUser: function () {
      var _headers = {};

      if (_token) {
        _headers = {
          Authorization: `Bearer ${_token}`,
          Session_ID: _session_id,
        };
      } else {
        this.hideModal();
        return;
      }

      const firstname = document.getElementById("firstname").value;
      const address = document.getElementById("_address").value;
      const is_superuser = document.getElementById("is_superuser").checked;

      console.log("firstname", firstname);
      console.log("address", address);
      console.log("is_superuser", is_superuser);

      const update_user_mutation = gql`
        mutation {
          update_user(
            user: { address: "${address}", firstname: "${firstname}", is_superuser: ${is_superuser} }
          ) {
            username
          }
        }
      `;
      console.log(update_user_mutation);

      request(url, update_user_mutation, null, _headers).then((data) => {
        console.log("Data", data);
        alert(`Updated user with username: ${data.update_user.username}`);
      });
      this.hideModal();
    },
    getUser: function () {
      var _headers = {};

      if (_token) {
        _headers = {
          Authorization: `Bearer ${_token}`,
          Session_ID: _session_id,
        };
      } else {
        this.hideModal();
        return;
      }

      console.log("Headers", _headers);

      const whoami_query = gql`
        query {
          whoami {
            firstname
            address
            username
            is_superuser
          }
        }
      `;
      request(url, whoami_query, null, _headers).then((data) => {
        console.log("Data", data);
        this.user_data = data.whoami;
      });
      this.hideModal();
    },
    hideModal: function () {
      this.$emit("show", 0);
    },
  },
};
</script>

<style scoped>
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