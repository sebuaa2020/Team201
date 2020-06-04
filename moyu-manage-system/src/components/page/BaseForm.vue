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
                            <el-option key="cruise" label="巡航" value="cruise"></el-option>
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
                    <el-form-item label="目的房间号(送物功能用)">
                        <el-checkbox-group v-model="form.type">
                            <el-checkbox label="101" name="type"></el-checkbox>
                            <el-checkbox label="102" name="type"></el-checkbox>
                            <el-checkbox label="103" name="type"></el-checkbox>
                        </el-checkbox-group>
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
                type: [101,102,103],
                desc: '',
                options: []
            }
        };
    },
    methods: {
        onSubmit() {
            this.form.region
            this.$message.success(this.form.region+'提交成功！');
        }
    }
};
</script>