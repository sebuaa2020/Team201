import request from '../utils/request';

export const fetchData = query => {
    return request({
        url: './table.json',
        method: 'get',
        params: query
    });
};

export const deliver = room_id => {
    return request({
        url: '/robot/deliver/',
        method: 'get',
        params: {'room_id': room_id}
    })
}

export const navigate = (source_x, source_y, target_x, target_y) => {
    return request({
        url: '/robot/navigate/',
        method: 'get',
        params: {'source_x': source_x, 'source_y': source_y, 'target_x':target_x, 'target_y': target_y}
    })
}

export const move_ctrl = command =>{
    return request({
        url: '/robot/move_ctrl/',
        method: 'get',
        params: {'command': command}
    })
}

export const voice_reg = () =>{
    return request({
        url: '/robot/voice_reg/',
        method: 'get',
        params:{}
    })
}

export const hector_mapping = () =>{
    return request({
        url: '/robot/hector_mapping/',
        method: 'get',
        params:{}
    })
}