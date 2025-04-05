require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: "0.8.28",
  networks: {
    polygon: {
      url: process.env.INFURA_URL, // Tu URL de Infura con /v3/TU_API_KEY
      accounts: [process.env.PRIVATE_KEY]
    },
    sepolia: {
      url: process.env.SEPOLIA_INFURA_URL,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
