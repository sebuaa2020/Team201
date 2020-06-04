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
                    <div align="center">
                    <img src="../../assets/img/map.jpg" />
                    </div>
                    <br>
                    <div align="center">
                        <el-button type="primary" @click="onSubmit">启动建图功能</el-button>
                    </div>
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
        hector_mapping_request(){
            hector_mapping().then(res=>{
                if (res.success){   
                    this.$message.success('正在执行！');
                }
                else{
                    this.$message.success('建图失败！请再尝试一次');
                }
            })
        },
        onSubmit() {
            this.hector_mapping_request()
        }
    }
};
</script>