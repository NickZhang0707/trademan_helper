import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Dashboard from "./Dashboard";
import Schedule from "./Schedule";
import Root from "./root";
import { CssVarsProvider } from '@mui/joy/styles';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children:[
      {
        index: true,
        element: <Dashboard />,
      },
      {
        path: "schedule",
        element: <Schedule />,
      }
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <CssVarsProvider>   {/* Joy UI 的主题上下文 */}
      <RouterProvider router={router} />
    </CssVarsProvider>
  </React.StrictMode>
);
