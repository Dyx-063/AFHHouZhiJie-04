<template>
  <div class="container">
    <h2>AI问答网页入口</h2>
    <textarea v-model="userQuestion" placeholder="请输入你的问题" rows="4"></textarea>
    <button @click="sendQuestion">提交提问</button>
    <div class="result-box">
      <h3>AI返回结果：</h3>
      <p>{{ answer }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const userQuestion = ref('')
const answer = ref('')

const sendQuestion = async () => {
  if (!userQuestion.value) return alert('请输入问题')
  try {
    const res = await axios.post('http://localhost:8000/chat', {
      question: userQuestion.value
    })
    answer.value = res.data.answer
  } catch (err) {
    answer.value = '请求出错：' + err.message
  }
}
</script>

<style scoped>
.container{width:800px;margin:30px auto;}
textarea{width:100%;margin:10px 0;padding:10px;}
button{padding:8px 20px;cursor:pointer;}
.result-box{margin-top:20px;padding:15px;border:1px solid #eee;}
</style>