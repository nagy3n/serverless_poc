import axios from 'axios'
export const HTTP = axios.create({
  baseURL: `http://localhost:5000/`,
  headers: {
    // Authorization: 'Bearer {token}'
  }
});