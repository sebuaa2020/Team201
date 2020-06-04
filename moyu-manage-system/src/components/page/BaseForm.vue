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
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="100px">
                    <el-form-item label="任务发起者">
                        <el-input v-model="form.name"></el-input>
                    </el-form-item>
                    <el-form-item label="任务类型">
                        <el-select v-model="form.task" placeholder="请选择">
                            <el-option key="direct" label="导航" value="direct"></el-option>
                            <el-option key="send" label="送物" value="send"></el-option>
                            <el-option key="mov_ctrl" label="人工控制" value="mov_ctrl"></el-option>
                            <el-option key="video_reg" label="语音识别" value="video_reg"></el-option>
                            <el-option key="hector_mapping" label="建图" value="hector_mapping"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="日期时间">
                        <el-col :span="11">
                            <el-date-picker
                                type="date"
                                placeholder="选择日期"
                                v-model="form.date1"
                                value-format="yyyy-MM-dd"
                                style="width: 100%;"
                            ></el-date-picker>
                        </el-col>
                        <el-col class="line" :span="2">-</el-col>
                        <el-col :span="11">
                            <el-time-picker
                                placeholder="选择时间"
                                v-model="form.date2"
                                style="width: 100%;"
                            ></el-time-picker>
                        </el-col>
                    </el-form-item>
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
                    <el-form-item label="目的房间号">
                        <el-radio-group v-model="form.type">
                            <el-radio label="101" name="type"></el-radio>
                            <el-radio label="102" name="type"></el-radio>
                            <el-radio label="103" name="type"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                     <el-form-item label="人工操作选择">
                        <el-radio-group v-model="form.type1">
                            <el-radio label="forward" name="type1"></el-radio>
                            <el-radio label="backward" name="type1"></el-radio>
                            <el-radio label="left" name="type1"></el-radio>
                            <el-radio label="right" name="type1"></el-radio>
                            <el-radio label="stop" name="type1"></el-radio>
                        </el-radio-group>
                    </el-form-item>
                    <el-form-item label="执行命令">
                        <el-input type="textarea" rows="5" v-model="form.desc"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">表单提交</el-button>
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
            if(this.form.task == "direct"){
                this.navigate_request(Number(this.form.start_x),Number(this.form.start_y),Number(this.form.end_x),Number(this.form.end_y))
            }
            else if(this.form.task == "send"){
                if(isNaN(Number(this.form.type))){
                    window.alert("抱歉，您的操作有误")
                    return;
                }
                this.deliver_request(Number(this.form.type))
            }
            else if(this.form.task == "mov_ctrl"){
                this.move_ctrl_request(this.form.type1)
            }
            else if(this.form.task == "video_reg"){
                this.voice_reg_request()
            }
            else if(this.form.task == "hector_mapping"){
                this.hector_mapping_request()
            }
            else{
                window.alert("指令错误")
            }
            
            //this.navigate_my(1,1,1,1)
            //var ans1 = this.navigate_my()
            //window.alert(ans1.url)
            //var test_ans = this.test()
            //if(test_ans.test_1){
            //    window.alert(test_ans.test_2)
            //}
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