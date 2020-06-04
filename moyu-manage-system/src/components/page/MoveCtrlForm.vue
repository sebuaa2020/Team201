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
                <el-form ref="form" :model="form" label-width="100px">
                    <el-form-item align="center">
                        <el-button type="primary" @click="forward">前进</el-button>
                        <el-button type="primary" @click="backward">后退</el-button>
                    </el-form-item>
                    <el-form-item align="center">
                        <el-button type="primary" @click="left">左移</el-button>
                        <el-button type="primary" @click="right">右移</el-button>
                    </el-form-item>
                    <el-form-item align="center">
                        <el-button type="primary" @click="stop">刹车</el-button>
                    </el-form-item>
                </el-form>
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
        move_ctrl_request(command){
            move_ctrl(command).then(res=>{
                if (res.success){   
                    this.$message.success('正在执行！');
                }
                else{
                    this.$message.success('抱歉，您的人工操作请求不符合规范');
                }
            })
        },
        forward() {
            this.move_ctrl_request("forward") 
        },
        backward() {
            this.move_ctrl_request("backward") 
        },
        left() {
            this.move_ctrl_request("left") 
        },
        right() {
            this.move_ctrl_request("right") 
        },
        stop() {
            this.move_ctrl_request("stop") 
        }
    }
};
</script>