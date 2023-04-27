<template>
    <div class="row">
        <div class="col-sm-10">
            <h1> API CRUD </h1>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col"> Title </th>
                        <th scope="col">Content</th>
                        <th scope="col">Publisher</th>
                        <th scope="col">Categories</th>
                        <th scope="col">Users</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody class="v-node" v-for="item in this.$store.state.products" :key="item.id">

                    <tr>

                        <td>{{ item.title }}</td>
                        <td>{{ item.content }}</td>
                        <td>{{ item.is_published }}</td>
                        <td>{{ item.cat }}</td>
                        <td>{{ item.user }}</td>

                        <td>
                            <button type="button" class="btn btn-warning btn-sm">Update</button>
                            <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </td>
                    </tr>

                </tbody>
            </table>

        </div>
    </div>

    <h1>Data Form</h1>
</template>

<script>
import { mapActions } from 'vuex';

export default {
    name: 'v-node',
    data() {
        return {
            priducts: [

            ]
        }
    },
    methods: {
        ...mapActions([
            'GET_PRODUCTS_API'
        ])
    },
    mounted() {
        this.GET_PRODUCTS_API()
    }
}
</script>   
<style>
.v-node {
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style> 
