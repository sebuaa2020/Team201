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
                    <el-table
                        :data="tableData"
                        border
                        class="table"
                        ref="multipleTable"
                        header-cell-class-name="table-header"
                        @selection-change="handleSelectionChange"
                    >   
                        <el-table-column type="index" label="序号" align="center"></el-table-column>
                        <el-table-column prop="room_id" label="房间号" align="center"></el-table-column>
                        <el-table-column prop="occupied" label="入住情况" align="center"></el-table-column>
                        <el-table-column label="操作" width="180" align="center">
                            <template slot-scope="scope">
                                <el-button
                                    type="primary"
                                    @click="onSubmit(scope.$index)">送物</el-button>
                            </template>
                        </el-table-column>
                     </el-table>
                    <br>
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
            },
            tableData: [
                {
                    "room_id": "101", 
                    "occupied": "已入住"
                },
                {
                    "room_id": "102", 
                    "occupied": "已入住"
                },
                {
                    "room_id": "103", 
                    "occupied": "已入住"
                },
                {
                    "room_id": "104", 
                    "occupied": "未入住"
                }
            ]
        };
    },
    methods: {
        deliver_request(room_id) {
            deliver(room_id).then(res => {
               if (res.success){   
                    this.$message.success('提交成功！');
                }
                else{
                    this.$message.error('抱歉，您的送货请求不符合规范');
                }
            });
        },
        onSubmit(index) {
            this.deliver_request(this.tableData[index].room_id)
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