<template>
  <div class="header">
    <div class="header_logo">
      <img
        class="header_logo_img"
        src="http://127.0.0.1:8000/static/header_logo.png"
      />
    </div>

    <div class="header_menu">
      <div class="header_menu_item">
        <img class="header_icon" src="http://127.0.0.1:8000/static/geo.png" />
        <span>Южно-Сахалинск</span>
      </div>
      <div class="header_menu_item">
        <img
          class="header_icon"
          src="http://127.0.0.1:8000/static/work_clock.png"
        />
        <span>Режим работы: с 11:00 до 23:00</span>
      </div>
    </div>

    <div class="header_menu_item phone">
      <img class="header_icon" src="http://127.0.0.1:8000/static/phone.png" />
      <span>
        <a href="tel:89621007559">8 (962) 100-75-59</a>
      </span>
    </div>

    <div class="login_btn" v-if="!this.token" @click="showModal()">
      <div>
        <a href="#login">Войти</a>
      </div>
    </div>

    <div class="login_btn" v-if="this.token" @click="deleteCookie()">
      <div>
        <a href="#login">Выйти</a>
      </div>
    </div>
  </div>
</template>

<script>
import cookies from "vue-cookies";

export default {
  data() {
    return {
      token: cookies.get("_token"),
    };
  },
  methods: {
    deleteCookie: function () {
      cookies.remove("_token");
      cookies.remove("_Session_ID");
    },
    showModal: function () {
      this.$emit("show", "login");
    },
  },
};
</script>


<style scoped>
.header {
  background-color: #ff5757;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  height: fit-content;
  width: 100%;
  margin-bottom: 3%;
  color: #fff;
  font-weight: 700;
}

.header_logo {
  width: 10%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-self: center;
  flex-wrap: wrap;
}

.header_logo img {
  height: 90px;
}

.header_menu {
  flex-direction: column;
  align-self: center;
  margin-left: 40px;
}

.header_icon {
  height: 30px;
  width: 30px;
}

.header_menu_item {
  display: flex;
  flex-direction: row;
  align-self: center;
  font-size: 1.5em;
}

.header_menu_item span {
  margin-left: 10px;
  align-self: center;
}

.phone {
  display: flex;
  margin-left: auto;
  text-shadow: -0 -1px 0 #000000, 0 -1px 0 #000000, -0 1px 0 #000000,
    0 1px 0 #000000, -1px -0 0 #000000, 1px -0 0 #000000, -1px 0 0 #000000,
    1px 0 0 #000000, -1px -1px 0 #000000, 1px -1px 0 #000000, -1px 1px 0 #000000,
    1px 1px 0 #000000, -1px -1px 0 #000000, 1px -1px 0 #000000,
    -1px 1px 0 #000000, 1px 1px 0 #000000;
}

/* .phone span a {
  box-shadow: 0px 0px 0px 4px #000;
} */

.login_btn {
  display: flex;
  background-color: #ffe9e5;
  height: 50px;
  width: 100px;
  font-size: 1.4em;
  font-weight: bold;
  border: none;
  border-radius: 30px;
  align-self: center;
  margin-left: auto;
  margin-right: 60px;
  cursor: pointer;
}

.login_btn div {
  align-self: center;
  margin: 0 auto;
}

.login_btn a {
  color: #ff5757;
}
</style>