<template>
    <v-app>
        <div id="nav">
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link> | 
            <router-link v-if="authenticated" to="/activities"
            v-on:click.native="setAuthenticated(true)" replace>学校近期活动安排</router-link> | 
            <router-link v-if="authenticated" to="/courses">课程表</router-link> | 
            <router-link v-if="authenticated" to="/students">学生登记表</router-link> |
            <router-link to="/combo">Combobox test</router-link>
        </div>
        <router-view @authenticated="setAuthenticated" />
    </v-app>
</template>

<script>
    export default {
        name: 'App',
        data() {
            return {
                authenticated: false,
                user: {}
            }
        },
        mounted() {
            if(!this.authenticated) {
                this.$router.replace({ name: "login" });
            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            }
        }
    }
</script>

<style>
    body {
        background-color: #F0F0F0;
    }
    h1 {
        padding: 0;
        margin-top: 0;
    }
    #app {
        width: 1024px;
        margin: auto;
    }
</style>