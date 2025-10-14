import * as React from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Copyright from './internals/components/Copyright';

import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import { DataGrid } from '@mui/x-data-grid';
import { columns, rows } from './internals/data/inspectionData';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';

const inspectionType = [
  { label: 'IFO - Foundation', value: 'IFO' },
  { label: 'ICB - Concrete block', value: 'ICB' },
  { label: 'ITK - Waterproofing Membrane (select for internal and external waterproofing)', value: 'ITK' },
  { label: 'IPP - Plumbing (underslab or plumbing preline)', value: 'IPP' },
  { label: 'ISF - Floor slab', value: 'ISF' },
  { label: 'IFG - Framing (select for Reclad strip-off or Reclad remedial)', value: 'IFG' },
  { label: 'ICA - Cavity Wrap', value: 'ICA' },
  { label: 'ICL - Cladding', value: 'ICL' },
  { label: 'IPB - Building preline (select when booking preline plumbing and preline building together)', value: 'IPB' },
  { label: 'IPL - Postline', value: 'IPL' },
  { label: 'IDT - Drainage', value: 'IDT' },
  { label: 'IF1 - Residential Final (select for Fireplace)', value: 'IF1' },
  { label: 'IME - Site Meeting', value: 'IME' },
  { label: 'Others', value: 'Others' },
];

const inspectionOtherType = [
  { label: 'IFO - Foundation', value: 'IFO' },
  { label: 'ICB - Concrete block', value: 'ICB' },
  { label: 'ITK - Waterproofing Membrane (select for internal and external waterproofing)', value: 'ITK' },
  { label: 'IPP - Plumbing (underslab or plumbing preline)', value: 'IPP' },
  { label: 'ISF - Floor slab', value: 'ISF' },
  { label: 'IFG - Framing (select for Reclad strip-off or Reclad remedial)', value: 'IFG' },
  { label: 'ICA - Cavity Wrap', value: 'ICA' },
  { label: 'ICL - Cladding', value: 'ICL' },
  { label: 'IPB - Building preline (select when booking preline plumbing and preline building together)', value: 'IPB' },
  { label: 'IPL - Postline', value: 'IPL' },
  { label: 'IDT - Drainage', value: 'IDT' },
  { label: 'IF1 - Residential Final (select for Fireplace)', value: 'IF1' },
  { label: 'IF2 - Commercial final', value: 'IF2' },
  { label: 'IME - Site Meeting', value: 'IME' },
  { label: 'CPU - Certificate of public use', value: 'CPU' },
  { label: 'PCO - Pre-construction Commercial', value: 'PCO' },
];







export default function InspectionGrid() {
  const [selectedType, setSelectedType] = React.useState(null);
  const [selectedOther, setSelectedOther] = React.useState(null);

  return (
    <Box sx={{ width: '100%', maxWidth: { sm: '100%', md: '1700px' } }}>
      {/* cards */}
      <Grid container spacing={2} columns={12} sx={{ mb: (theme) => theme.spacing(2) }}>
        <Grid size={{ xs: 12, sm: 12, lg: 12 }}>
          <Stack spacing={2}>
            <Typography variant="h6" sx={{ mb: 2 }}>
              Book an inspection
            </Typography>

            <Typography variant="h8" sx={{ mb: 2 }}>
              BCO
            </Typography>
            <TextField id="BCO" label="BCO" variant="outlined" sx={{ width: 220 }} />

            <Typography variant="h8" sx={{ mb: 2 }}>
              Select inspection type
            </Typography>

            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <Autocomplete
                disablePortal
                options={inspectionType}
                getOptionLabel={(option) => option.label}
                sx={{ width: 650 }}
                value={selectedType}
                onChange={(event, newValue) => {
                  setSelectedType(newValue);
                  if (newValue?.value !== 'Others') {
                    setSelectedOther(null);
                  }
                }}
                renderInput={(params) => <TextField {...params} label="Choose an inspection Type..." />}
              />

              {selectedType?.value === 'Others' && (
                <Stack spacing={2}>
                    <Typography variant="h8" sx={{ mb: 2 }}>
                      Other inspection type
                    </Typography>
                    <Autocomplete
                    disablePortal
                    options={inspectionOtherType}
                    getOptionLabel={(option) => option.label}
                    sx={{ width: 650 }}
                    value={selectedOther}
                    onChange={(event, newValue) => setSelectedOther(newValue)}
                    renderInput={(params) => (
                        <TextField {...params} label="Choose an inspection Type..." />
                    )}
                    />
                </Stack>
              )}
            </Box>

            <Stack direction="row" spacing={2} sx={{ mt: 2 }}>
                <Typography variant="h8" sx={{ mb: 3, width: 220 }}>
                Start date
                </Typography>
                

                <Typography variant="h8" sx={{ mb: 3, width: 220 }}>
                End date
                </Typography>
                
            </Stack>
            <Stack direction="row" spacing={2} sx={{ mt: 2 }}>
                <TextField
                id="date"
                label="Start Date"
                type="date"
                defaultValue={new Date().toISOString().split('T')[0]}
                sx={{ width: 220 }}
                InputLabelProps={{ shrink: true }}
                />
                <TextField
                id="date"
                label="End Date"
                type="date"
                defaultValue={new Date().toISOString().split('T')[0]}
                sx={{ width: 220 }}
                InputLabelProps={{ shrink: true }}
                />
            </Stack>
            <Stack direction="row" spacing={2} sx={{ mt: 2 }}>
                <Typography variant="h8" sx={{ mb: 2, width: 220 }}>
                    myAuckland user name
                </Typography>
                <Typography variant="h8" sx={{ mb: 2, width: 220 }}>
                    myAuckland password
                </Typography>
                <Typography variant="h8" sx={{ mb: 2, width: 220 }}>
                Onsite contact name
                </Typography>
                <Typography variant="h8" sx={{ mb: 2, width: 220 }}>
                Onsite contact phone number
                </Typography>

            </Stack>
            <Stack direction="row" spacing={2} sx={{ mt: 2 }}>
                <TextField id="myAklUserName" label="myAuckland user name" variant="outlined" sx={{ width: 220 }} />
                <TextField id="myAklPassword" label="myAuckland password" variant="outlined" sx={{ width: 220 }} />
                <TextField id="onSiteContectName" label="Onsite contact name" variant="outlined" sx={{ width: 220 }} />                
                <TextField id="onSiteContectPhoneNum" label="Onsite contact phone number" variant="outlined" sx={{ width: 220 }} />
            </Stack>

            <Typography variant="h8" sx={{ mb: 2 }}>
              Onsite contact email
            </Typography>
            <Stack direction="row" spacing={2} sx={{ mt: 2 }}>
                <TextField id="onSiteContectEmail" label="Onsite contact email" variant="outlined" sx={{ width: 220 }} />
                <Button variant="contained">Submit</Button>
            </Stack>
          </Stack>
            
        </Grid>

      </Grid>

      <Divider sx={{mt: 5, mb:5}} />

      <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
        Booking History
      </Typography>
      <Grid container spacing={2} columns={12}>
        <Grid size={{ xs: 12, lg: 9 }}> 
          <DataGrid
                // checkboxSelection
                disableRowSelectionOnClick
                rows={rows}
                columns={columns}
                getRowClassName={(params) =>
                  params.indexRelativeToCurrentPage % 2 === 0 ? 'even' : 'odd'
                }
                initialState={{
                  pagination: { paginationModel: { pageSize: 20 } },
                }}
                pageSizeOptions={[10, 20, 50]}
                disableColumnResize
                density="compact"
                slotProps={{
                  filterPanel: {
                    filterFormProps: {
                      logicOperatorInputProps: {
                        variant: 'outlined',
                        size: 'small',
                      },
                      columnInputProps: {
                        variant: 'outlined',
                        size: 'small',
                        sx: { mt: 'auto' },
                      },
                      operatorInputProps: {
                        variant: 'outlined',
                        size: 'small',
                        sx: { mt: 'auto' },
                      },
                      valueInputProps: {
                        InputComponentProps: {
                          variant: 'outlined',
                          size: 'small',
                        },
                      },
                    },
                  },
                }}
                // sx={{width: 1500}}
              />
        </Grid>
      </Grid>

      {/* Copyright */}
      <Copyright sx={{ my: 4 }} />
    </Box>
  );
}
