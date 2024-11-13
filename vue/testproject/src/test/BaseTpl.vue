<template>
    <h1>{{msgh1}}</h1>
</template>
<script>
export default {
    name:'BaseTpl',
    props:{
        msgh1:String
    }
}
</script>

<style lang="css" scoped>
h1{
    color:#005bd1;
    font-weight: bold;
}
</style>