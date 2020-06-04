<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> 表单
                </el-breadcrumb-item>
                <el-breadcrumb-item>任务表单</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                
                    <div align="center">
                    <img src="../../assets/img/voice_reg.jpg" />
                    </div>
                    <br>
                    <div align="center">
                        <el-button type="primary" @click="onSubmit">启动语音识别</el-button>
                    </div>
            
            </div>
        </div>
    </div>
</template>

<script>
import {fetchData,deliver,navigate,move_ctrl,voice_reg,hector_mapping } from '../../api/index';
import request from '../../utils/request';
export default {
    name: 'baseform',
    data() {
        return {
            form: {
            }
        };
    },
    methods: {
        voice_reg_request(){
            voice_reg().then(res=>{
                if (res.success){   
                    this.$message.success('正在执行！');
                }
                else{
                    this.$message.success('抱歉，我没听清，请再说一次');
                }
            })
        },
        onSubmit() {
            this.voice_reg_request()
        }
    }
};
</script>