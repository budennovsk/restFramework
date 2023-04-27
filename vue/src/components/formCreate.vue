<template>
    <form @submit.prevent="createPostw">
        <div>
            <label class="col-form-label" for="pos">Post User id</label>
            <input type="text" id="pos" v-model="formData.pos" />
        </div>
        <div>
            <label class="col-form-label" for="title">Post Title</label>
            <input type="text" id="title" v-model="formData.title" />
        </div>
        <div>
            <label for="content">Post Content</label>
            <input type="text" id="content" v-model="formData.content" />
        </div>

        <div>
            <label for="pudlished">Post Published</label>
            <input type="text" id="pudlished" v-model="formData.pudlished" />
        </div>
        <div>
            <label for="category">Post Category</label>
            <input type="text" id="category" v-model="formData.category" />
        </div>
        
        <button type="button" class="btn btn-success">Create Post</button>

    </form>
</template>

<script>

import axios from 'axios';

export default {
    name: 'v-post',
    data() {
        return {
            formData: {
                pos: '12',
                title: "21",
                content: "",
                time_create: '1',
                time_update: '1',
                is_published: true,
                cat: 1,
                user: 1
            },


        }
    },
    methods: {
        createPostw() {
            axios.post('http://127.0.0.1:8000/', this.formData)
                

                .then((response) => {
                    this.formData = response.data
                })
                .catch(error => console.error(error))

        }
    },

};
</script>   
<style>
.v-node {
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style> 
