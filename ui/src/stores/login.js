import { defineStore } from 'pinia';

export const useLoginStore = defineStore('login', {
    state() {
        return {
            userInfo: {},
        };
    },
    actions: {
        updateUserInfo(userInfo) {
            this.userInfo = userInfo;
        },
        toggleSidebar() {
            this.isSidebarOpen = !this.isSidebarOpen;
        },
    },
    strict: process.env.DEBUGGING,
});
