import { defineStore } from "pinia";
import dayjs from 'dayjs';

import axios from 'axios';
import { cacheAdapterEnhancer } from 'axios-extensions';

const api = axios.create({
  headers: { 'Cache-Control': 'no-cache' },
  adapter: cacheAdapterEnhancer(axios.getAdapter(axios.defaults.adapter)),
});

// const apiUrl = process.env.VUE_APP_API_URL
const apiUrl = "http://localhost:8000";

api.interceptors.response.use(
  (response) => {

    return response;
  },
  (err) => {
    if (err.response.status === 404) {
      window.location.href = "/404";
    }

    return Promise.reject(err);
  }
);

async function getContent(id) {
  const response = await api.get(apiUrl + '/notice/' + id);
  return response.data;
}


async function getSummary(id) {
  const response = await api.get(apiUrl + '/notice?page=' + id);
  return response.data;
}



export const useNoticeStore = defineStore("noticeStore", {

  state: () => ({
    notice: Object,
    notices: [],
    nowPage: 1,
    loading: false,
    totalPage: 0,
  }),


  getters: {

  },

  actions: {
    async loadPost(id) {
      this.loading = true;

      this.notice = '';
      this.notice = await getContent(id);

      this.loading = false;
    },

    async loadPostList(id) {
      this.loading = true;

      this.notices = '';
      let data = await getSummary(id);

      this.totalPage = data.total_page;
      this.notices = data.notice_list;

      this.loading = false;
    },

    formatDate(dateString) {
      const date = dayjs(dateString);

      return date.format('YYYY.MM.DD HH:mm');
    },

    getNoticeTypeClass(noticeType) {
      switch (noticeType) {
        case 'UPDATE':
          return 'success';
        case 'FIX':
          return 'warning';
        case 'RESERVED_CHECK':
          return 'error';
        default:
          return "success";
      }
    },


    noticeTypeToKorean(noticeType) {
      switch (noticeType) {
        case 'UPDATE':
          return '업데이트';
        case 'FIX':
          return '오류수정';
        case 'RESERVED_CHECK':
          return '점검예정';
        default:
          return "공지사항";
      }
    },




    // # UPDATE("업데이트"),
    // # FIX("오류수정"),
    // # RESERVED_CHECK("점검예정")
  }
});
