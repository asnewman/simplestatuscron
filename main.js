const axios = require("axios").default;

axios.post("https://simplestat.us/api/check").then(() => {
  console.log("Success!");
}).catch((err) => {
  console.error(err);
}