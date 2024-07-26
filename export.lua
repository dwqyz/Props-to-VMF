local function export_props()
    local file = file.Open("props_export.txt", "w", "DATA")
    
    for _, ent in ipairs(ents.GetAll()) do
        if ent:GetClass() == "prop_physics" then
            local model = ent:GetModel()
            local pos = ent:GetPos()
            local ang = ent:GetAngles()
            file:Write(string.format("%s %s %.6f %.6f %.6f %.3f %.3f %.3f\n", 
                ent:GetClass(), 
                model, 
                pos.x, pos.y, pos.z, 
                ang.p, ang.y, ang.r))
        end
    end
    
    file:Close()
end

concommand.Add("export_props", export_props)
