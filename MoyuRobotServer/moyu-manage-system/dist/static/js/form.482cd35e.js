(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["form"],{ec6b:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("div",{staticClass:"crumbs"},[s("el-breadcrumb",{attrs:{separator:"/"}},[s("el-breadcrumb-item",[s("i",{staticClass:"el-icon-lx-calendar"}),e._v(" 表单\n            ")]),s("el-breadcrumb-item",[e._v("任务表单")])],1)],1),s("div",{staticClass:"container"},[s("div",{staticClass:"form-box"},[s("el-form",{ref:"form",attrs:{model:e.form,"label-width":"100px"}},[s("el-form-item",{attrs:{label:"任务发起者"}},[s("el-input",{model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),s("el-form-item",{attrs:{label:"任务类型"}},[s("el-select",{attrs:{placeholder:"请选择"},model:{value:e.form.task,callback:function(t){e.$set(e.form,"task",t)},expression:"form.task"}},[s("el-option",{key:"direct",attrs:{label:"导航",value:"direct"}}),s("el-option",{key:"send",attrs:{label:"送物",value:"send"}}),s("el-option",{key:"mov_ctrl",attrs:{label:"人工控制",value:"mov_ctrl"}}),s("el-option",{key:"video_reg",attrs:{label:"语音识别",value:"video_reg"}}),s("el-option",{key:"hector_mapping",attrs:{label:"建图",value:"hector_mapping"}})],1)],1),s("el-form-item",{attrs:{label:"日期时间"}},[s("el-col",{attrs:{span:11}},[s("el-date-picker",{staticStyle:{width:"100%"},attrs:{type:"date",placeholder:"选择日期","value-format":"yyyy-MM-dd"},model:{value:e.form.date1,callback:function(t){e.$set(e.form,"date1",t)},expression:"form.date1"}})],1),s("el-col",{staticClass:"line",attrs:{span:2}},[e._v("-")]),s("el-col",{attrs:{span:11}},[s("el-time-picker",{staticStyle:{width:"100%"},attrs:{placeholder:"选择时间"},model:{value:e.form.date2,callback:function(t){e.$set(e.form,"date2",t)},expression:"form.date2"}})],1)],1),s("el-form-item",{attrs:{label:"起始地x坐标"}},[s("el-input",{model:{value:e.form.start_x,callback:function(t){e.$set(e.form,"start_x",t)},expression:"form.start_x"}})],1),s("el-form-item",{attrs:{label:"起始地y坐标"}},[s("el-input",{model:{value:e.form.start_y,callback:function(t){e.$set(e.form,"start_y",t)},expression:"form.start_y"}})],1),s("el-form-item",{attrs:{label:"目的地x坐标"}},[s("el-input",{model:{value:e.form.end_x,callback:function(t){e.$set(e.form,"end_x",t)},expression:"form.end_x"}})],1),s("el-form-item",{attrs:{label:"目的地y坐标"}},[s("el-input",{model:{value:e.form.end_y,callback:function(t){e.$set(e.form,"end_y",t)},expression:"form.end_y"}})],1),s("el-form-item",{attrs:{label:"目的房间号"}},[s("el-radio-group",{model:{value:e.form.type,callback:function(t){e.$set(e.form,"type",t)},expression:"form.type"}},[s("el-radio",{attrs:{label:"101",name:"type"}}),s("el-radio",{attrs:{label:"102",name:"type"}}),s("el-radio",{attrs:{label:"103",name:"type"}})],1)],1),s("el-form-item",{attrs:{label:"人工操作选择"}},[s("el-radio-group",{model:{value:e.form.type1,callback:function(t){e.$set(e.form,"type1",t)},expression:"form.type1"}},[s("el-radio",{attrs:{label:"forward",name:"type1"}}),s("el-radio",{attrs:{label:"backward",name:"type1"}}),s("el-radio",{attrs:{label:"left",name:"type1"}}),s("el-radio",{attrs:{label:"right",name:"type1"}}),s("el-radio",{attrs:{label:"stop",name:"type1"}})],1)],1),s("el-form-item",{attrs:{label:"执行命令"}},[s("el-input",{attrs:{type:"textarea",rows:"5"},model:{value:e.form.desc,callback:function(t){e.$set(e.form,"desc",t)},expression:"form.desc"}})],1),s("el-form-item",[s("el-button",{attrs:{type:"primary"},on:{click:e.onSubmit}},[e._v("表单提交")]),s("el-button",[e._v("取消")])],1)],1)],1)])])},r=[],l=(s("163d"),s("365c")),o=s("b775"),i={name:"baseform",data:function(){return{form:{name:"",task:"",date1:"",date2:"",start_x:"",start_y:"",end_x:"",end_y:"",type:[],type1:[],desc:"",options:[]}}},methods:{fetchData_request:function(e){var t=this;Object(l["a"])(e).then((function(e){e.success?t.$message.success("提交成功！"):t.$message.success("抱歉，您的取物请求不符合规范")}))},deliver_request:function(e){var t=this;Object(l["a"])(e).then((function(e){e.success?t.$message.success("提交成功！"):t.$message.success("抱歉，您的送货请求不符合规范")}))},navigate_request:function(e,t,s,a){var r=this;Object(l["e"])(e,t,s,a).then((function(e){e.success?r.$message.success("提交成功！"):r.$message.success("抱歉，您的巡航请求不符合规范")}))},move_ctrl_request:function(e){var t=this;Object(l["d"])(e).then((function(e){e.success?t.$message.success("正在执行！"):t.$message.success("抱歉，您的人工操作请求不符合规范")}))},voice_reg_request:function(){var e=this;Object(l["f"])().then((function(t){t.success?e.$message.success("正在执行！"):e.$message.success("抱歉，我没听清，请再说一次")}))},hector_mapping_request:function(){var e=this;Object(l["c"])().then((function(t){t.success?e.$message.success("正在执行！"):e.$message.success("建图失败！请再尝试一次")}))},onSubmit:function(){if("direct"==this.form.task)this.navigate_request(Number(this.form.start_x),Number(this.form.start_y),Number(this.form.end_x),Number(this.form.end_y));else if("send"==this.form.task){if(isNaN(Number(this.form.type)))return void window.alert("抱歉，您的操作有误");this.deliver_request(Number(this.form.type))}else"mov_ctrl"==this.form.task?this.move_ctrl_request(this.form.type1):"video_reg"==this.form.task?this.voice_reg_request():"hector_mapping"==this.form.task?this.hector_mapping_request():window.alert("指令错误")},navigate_my:function(e,t,s,a){return window.alert("im in"),Object(o["a"])({url:"/robot/navigate/",method:"get",params:{source_x:e,source_y:t,target_x:s,target_y:a}})},test:function(){return window.alert("im in test"),this.test1(!0)},test1:function(e){return window.alert("im in test1"),!0===e?window.alert("true"):window.alert("false"),{test_1:!0,test_2:"nice"}}}},n=i,c=s("4023"),m=Object(c["a"])(n,a,r,!1,null,null,null);t["default"]=m.exports}}]);