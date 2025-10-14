import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Chip from '@mui/material/Chip';
import Button from '@mui/material/Button';


function renderStatus(status) {
  const colors = {
    Booked: 'success',
    Pending: 'default',
  };

  return <Chip label={status} color={colors[status]} size="small" />;
}



const stopBtn = <Button variant="contained" color='error' size="small">Stop</Button>;

function renderStopBtn(btnStatus) {
  if (btnStatus === 'Able') {
    return <Button variant="contained" color='error' size="small">Stop</Button>;
  } else {
    return null;
  }
}

export function renderAvatar(params) {
  if (params.value == null) {
    return '';
  }

  return (
    <Avatar
      sx={{
        backgroundColor: params.value.color,
        width: '24px',
        height: '24px',
        fontSize: '0.85rem',
      }}
    >
      {params.value.name.toUpperCase().substring(0, 1)}
    </Avatar>
  );
}



export const columns = [
  { field: 'btnStatus', 
    headerName: 'btnStatus', 
    flex: 0.5, 
    minWidth: 90, 
    renderCell: (params) => renderStopBtn(params.value),
  },
  { field: 'BCO', headerName: 'BCO', flex: 1.5, minWidth: 100 },
  {
    field: 'status',
    headerName: 'Status',
    flex: 0.5,
    minWidth: 110,
    renderCell: (params) => renderStatus(params.value),
  },
  {
    field: 'inspectionType',
    headerName: 'Inspection type',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 120,
  },
  {
    field: 'startDate',
    headerName: 'Start Date',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 100,
  },
  {
    field: 'endDate',
    headerName: 'End Date',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 100,
  },
  {
    field: 'myAucklandUserName',
    headerName: 'myAuckland user name',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 200,
  },
  {
    field: 'onSiteContactName',
    headerName: 'Onsite contact name',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 120,
  },
  {
    field: 'onSiteContactPhoneNum',
    headerName: 'Onsite contact phone number',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 150,
  },
  {
    field: 'onSiteContactEmail',
    headerName: 'Onsite contact email',
    headerAlign: 'right',
    align: 'right',
    flex: 1,
    minWidth: 200,
  }
];

export const rows = [
  {
    id: 1,
    BCO: 'BCO12345678',
    inspectionType: 'IFO - Foundation',
    startDate: '2024-04-01',
    endDate: '2024-04-02',
    myAucklandUserName: 'xzhang000999@gmail.com',
    onSiteContactName: 'Jane Smith',
    onSiteContactPhoneNum: '0291217466',
    onSiteContactEmail: 'xzhang000999@gmail.com',
    status: 'Booked', 
    btnStatus: 'Disable',
  },
  {
    id: 2,
    BCO: 'BCO12345678',
    inspectionType: 'IFO - Foundation',
    startDate: '2024-04-01',
    endDate: '2024-04-02',
    myAucklandUserName: 'john_doe',
    onSiteContactName: 'Jane Smith',
    onSiteContactPhoneNum: '555-1234',
    onSiteContactEmail: 'a@gmail.com',
    status: 'Pending', 
    btnStatus: 'Able',
  },
  {
    id: 3,
    BCO: 'BCO12345678',
    inspectionType: 'IFO - Foundation',
    startDate: '2024-04-01',
    endDate: '2024-04-02',
    myAucklandUserName: 'john_doe',
    onSiteContactName: 'Jane Smith',
    onSiteContactPhoneNum: '555-1234',
    onSiteContactEmail: 'a@gmail.com',
    status: 'Pending', 
    btnStatus: 'Able',
  },

  
];
