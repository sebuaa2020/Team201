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
        <div class="container" align="center">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="100px">
                    <el-form-item label="起始地x坐标">
                        <el-input v-model="form.start_x"></el-input>
                    </el-form-item>
                    <el-form-item label="起始地y坐标">
                        <el-input v-model="form.start_y"></el-input>
                    </el-form-item>
                    <el-form-item label="目的地x坐标">  
                        <el-input v-model="form.end_x"></el-input>
                    </el-form-item>
                    <el-form-item label="目的地y坐标">
                        <el-input v-model="form.end_y" ></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">执行任务</el-button>
                        <el-button>取消</el-button>
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
                name: '',
                task: '',
                date1: '',
                date2: '',
                start_x:'',
                start_y:'',
                end_x:'',
                end_y:'',
                type: [],
                type1:[],
                desc: '',
                options: []
            }
        };
    },
    methods: {
        fetchData_request(query){
            deliver(query).then(res => {
                if (res.success){   
                    this.$message.success('提交成功！');
                }
                else{
                    this.$message.success('抱歉，您的取物请求不符合规范');
                }
            });
        },
        deliver_request(room_id) {
            deliver(room_id).then(res => {
               if (res.success){   
                    this.$message.success('提交成功！');
                }
                else{
                    this.$message.success('抱歉，您的送货请求不符合规范');
                }
            });
        },
        navigate_request(source_x, source_y, target_x, target_y){
            navigate(source_x, source_y, target_x, target_y).then(res =>{
               if (res.success){   
                    this.$message.success('提交成功！');
                }
                else{
                    this.$message.success('抱歉，您的巡航请求不符合规范');
                }
            })
        },
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
            this.navigate_request(Number(this.form.start_x),Number(this.form.start_y),Number(this.form.end_x),Number(this.form.end_y))
        },
        navigate_my:function(source_x,source_y,target_x,target_y){
            window.alert("im in")
            return request({
                    url: '/robot/navigate/',
                    method: 'get',
                    params: {'source_x': source_x, 'source_y': source_y, 'target_x':target_x, 'target_y': target_y}
            }) 
        },
        test:function(){
            window.alert("im in test")
            return this.test1(true)
        },
        test1:function(test1){
            window.alert("im in test1")
            if(test1 === true){
                window.alert("true")
            }
            else{
                window.alert("false")
            }
            return {
                test_1: true,
                test_2:"nice"
            }
        },

    }
};
</script>