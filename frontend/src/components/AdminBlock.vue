<template>
  <div class="Admin_Block" v-if="showModal == 'admin'">
    <div class="header">Администратор
        <button id="cross" @click="hideModal()">
            <img id="cross" src="http://127.0.0.1:8000/static/cross.svg" />
        </button>
    </div>
    <div class="info_block">
    </div>
      <TicketBlock v-for="ticket in tickets" :key="ticket.id_" :ticket="ticket" />
    </div>
</template>

<script>
import { request, gql } from "graphql-request";
// import { v4 as uuid4 } from "uuid";
// import cookies from "vue-cookie";
import TicketBlock from "@/components/TicketBlock";

var url = "http://127.0.0.1:8000/graphql";

export default {
  props: ["showModal"],

  data() {
    return {
      tickets: this.getTickets(),
    };
  },
  components: {
    TicketBlock,
  },

  methods: {
    hideModal: function () {
      this.$emit("show", 0);
    },

    getTickets: function () {
      const ticket_query = gql`
        query {
          ticket {
            address
            final_price
            id_
            items
            status
            username
          }
        }
      `;
      request(url, ticket_query).then((data) => {
        this.tickets = data.ticket;
      });
    },
  },
};
</script>
<style scoped>
.Admin_Block {
  width: 50%;
  position: absolute;
  top: 0;
  left: 20;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  padding: 0% 1%;
  z-index: 100;
  border-radius: 15px;
}

.header {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  font-size: 150%;
  font-weight: 700;
  padding-top: 5%;
  border-bottom: 2px solid #000;   
}

#cross {
  width: 30px;
  margin-left: auto;
  margin-right: 5%;
  margin-top: -5%;
  background: none;
  border: none;
  cursor: pointer;
}
</style>