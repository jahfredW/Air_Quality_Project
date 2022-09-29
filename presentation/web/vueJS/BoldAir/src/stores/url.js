import { defineStore } from 'pinia'


export const useUrlStore = defineStore('url', () => {
  const urlMain = "http://127.0.0.1:8001/previsions"
  const ipMain = "127.0.0.1"
  const portMain = "8001"

  return {  urlMain, ipMain, portMain  }
})