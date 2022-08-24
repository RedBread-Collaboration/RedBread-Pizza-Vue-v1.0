<template>
  <div id="app">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Rokkitt:wght@700&display=swap"
      rel="stylesheet"
    />
    <div id="header">
      <HeaderDiv @show="updateShow($event)" />
    </div>
    <div id="body">
      <div>
        <navigation id="navigation">
          <div id="tab" @click="updateShow('profile')">
            <button id="tab_button"><span>Профиль</span></button>
          </div>
          <div id="tab">
            <div id="a" @click="updateShow('admin')">
              <button id="tab_button">
                <span>Админка</span>
              </button>
            </div>
          </div>
          <div id="tab" @click="updateShow('cart')">
            <button id="tab_button">
              <span>Корзина</span>
            </button>
          </div>
        </navigation>
      </div>
      <div id="center">
        <LoginBlock :showModal="showModalWin" @show="updateShow($event)" />
        <RegisterBlock :showModal="showModalWin" @show="updateShow($event)" />
        <TicketBlock :showModal="showModalWin" @show="updateShow($event)" />
        <ProfilePage :showModal="showModalWin" @show="updateShow($event)" />
        <AdminBlock :showModal="showModalWin" @show="updateShow($event)" />
        <BasketStore
          :showModal="showModalWin"
          @show="updateShow($event)"
          @updateCount="getCartSize($event)"
          @updateCart="updateUserCart()"
        ></BasketStore>
        <PizzaCard
          v-for="pizza in pizzas"
          :key="pizza.id_"
          :pizza="pizza"
          @show="updateShow($event)"
        />
      </div>
      <IngridientsItems
        v-for="pizza in pizzas"
        :key="pizza.id_"
        :pizza="pizza"
        @show="updateShow($event)"
        :showModal="showModalWin"
      />
    </div>
    <FooterDiv />
  </div>
</template>

<script>
import PizzaCard from "@/components/PizzaCard";
import IngridientsItems from "@/components/IngridientsItems";
import HeaderDiv from "@/components/HeaderDiv";
import FooterDiv from "@/components/FooterDiv";
import BasketStore from "@/components/BasketStore";
import LoginBlock from "@/components/LoginBlock";
import RegisterBlock from "@/components/RegisterBlock";
import ProfilePage from "@/components/ProfilePage";
// import TicketBlock from "@/components/TicketBlock";
import AdminBlock from "@/components/AdminBlock";

import { request, gql } from "graphql-request";
// import { v4 as uuid4 } from "uuid";

var url = "http://127.0.0.1:8000/graphql";

export default {
  name: "App",
  data() {
    return {
      pizzas: this.getAllPizzas(),
      counter: 0,
      showModalWin: 0,
    };
  },
  components: {
    PizzaCard,
    IngridientsItems,
    HeaderDiv,
    FooterDiv,
    BasketStore,
    LoginBlock,
    RegisterBlock,
    ProfilePage,
    // TicketBlock,
    AdminBlock,
  },
  
  methods: {
    updateShow: function (val) {
      console.log(val);
      this.showModalWin = val;
      console.log(this.showModalWin);
    },
    getAllPizzas: function () {
      const query = gql`
        query {
          pizza {
            id_
            ingredients
            name
            photo
            price_small
          }
        }
      `;
      request(url, query).then((data) => {
        // console.log(data.pizza);
        this.pizzas = data.pizza;
        // return pizzas;
      });
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  width: 10px; /* ширина для вертикального скролла */
  background-color: #f09090;
}

/* ползунок скроллбара */
::-webkit-scrollbar-thumb {
  background-color: #d60019;
  border-radius: 9em;
  box-shadow: inset 1px 1px 10px #f3faf7;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #253861;
}

/* Стрелки */

::-webkit-scrollbar-button:vertical:start:decrement {
  background: linear-gradient(120deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(240deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(0deg, #02141a 30%, rgba(0, 0, 0, 0) 31%);
  background-color: #f6f8f4;
}

::-webkit-scrollbar-button:vertical:end:increment {
  background: linear-gradient(300deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(60deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(180deg, #02141a 30%, rgba(0, 0, 0, 0) 31%);
  background-color: #f6f8f4;
}

::-webkit-scrollbar-button:horizontal:start:decrement {
  background: linear-gradient(30deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(150deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(270deg, #02141a 30%, rgba(0, 0, 0, 0) 31%);
  background-color: #f6f8f4;
}

::-webkit-scrollbar-button:horizontal:end:increment {
  background: linear-gradient(210deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(330deg, #02141a 40%, rgba(0, 0, 0, 0) 41%),
    linear-gradient(90deg, #02141a 30%, rgba(0, 0, 0, 0) 31%);
  background-color: #f6f8f4;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  overflow-x: hidden;
}

* {
  margin: 0;
  padding: 0;
}
a {
  text-decoration: none;
  color: #fff;
}

#body {
  display: flex;
  flex-direction: column;
  height: fit-content;
}

#navigation {
  width: max-width;
  height: fit-content;
  margin-bottom: 5%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

#tab_button {
  width: 100%;
  outline: none;
  background: none;
  border: none;
  cursor: pointer;
  font-family: "Roboto";
  font-weight: 700;
  font-size: 20px;
  color: #be0000;
}

#tab {
  width: 30%;
  height: 40px;
  box-shadow: 16px 16px 16px #00000040;
  border-radius: 15px;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

#a {
  width: 100%;
  cursor: pointer;
}

#center {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
